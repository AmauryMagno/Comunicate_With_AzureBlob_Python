import streamlit as st
from azure.storage.blob import BlobServiceClient
import os
import pymssql
import uuid
import json
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

# Connect to blob storage
blobConnectionString = os.getenv("BLOB_CONNECTION_STRING")
blobContainerName = os.getenv("BLOB_CONTAINER_NAME")
blobContainerSAS = os.getenv("BLOB_CONTAINER_SAS")
blobAccountName = os.getenv("BLOB_ACCOUNT_NAME")

# Connect to SQL database
SQL_SERVER = os.getenv("SQL_SERVER")
SQL_DATABASE = os.getenv("SQL_DATABASE")
SQL_USER = os.getenv("SQL_USER")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")

st.title("Cadastro de Produtos")

# Formulário de cadastro de produtos
product_name = st.text_input("Nome do Produto")
product_price = st.number_input("Preço do Produto", min_value=0.0, format="%.2f")
product_description = st.text_area("Descrição do Produto")
product_image = st.file_uploader("Imagem do Prduto", type=["jpg", "png", "jpeg"])


# Save imagem in blob storage
def upload_blob(file):
    blob_service_client = BlobServiceClient.from_connection_string(blobConnectionString)
    container_client = blob_service_client.get_container_client(blobContainerName)
    blob_name = str(uuid.uuid4()) + file.name
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file.read(), overwrite=True)
    image_url = f"https://{blobAccountName}.blob.core.windows.net/{blobContainerName}/{blob_name}"
    return image_url


def connect_databse():
    conn = pymssql.connect(
        server=SQL_SERVER,
        user=SQL_USER,
        password=SQL_PASSWORD,
        database=SQL_DATABASE,
    )
    return conn


def insert_product(product_name, product_price, product_description, product_image):
    try:
        image_url = upload_blob(product_image)
        conn = connect_databse()
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO Products (name, price, description, image_url) VALUES('{product_name}', '{product_price}', '{product_description}', '{image_url}')"
        )
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Erro ao inserir Produto: {e}")
        return False


def list_products():
    try:
        conn = connect_databse()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        st.error(f"Erro ao listar produtos: {e}")
        return []


def list_product_show():
    products = list_products()
    print(products)
    if products:
        # Define number of cadrs per row
        card_per_row = 3
        # Creat firts columns
        cols = st.columns(card_per_row)
        for i, product in enumerate(products):
            col = cols[i % card_per_row]
            with col:
                st.markdown(f"### {product[1]}")
                st.write(f"**Descrição:** {product[2]}")
                st.write(f"**Preço** R$ {product[3]: .2f}")
                if product[4]:
                    html_img = f'<img src="{product[4]}?{blobContainerSAS}" width="200" height="200"/>'
                    print(f"Imagem com SAS: {html_img}")
                    st.markdown(html_img, unsafe_allow_html=True)
                st.markdown("----")

            if (i + 1) % card_per_row == 0 and (i + 1) < len(products):
                cols = st.columns(card_per_row)
    else:
        st.info("Nenhum produto encontrado")


if st.button("Salvar Produto"):
    insert_product(product_name, product_price, product_description, product_image)
    return_message = "Produto Salvo com Sucesso"
    list_product_show()


st.header("Produtos Cadastrados")

if st.button("Listar Produtos"):
    list_product_show()
    return_message = "Produtos listados com sucesso"
