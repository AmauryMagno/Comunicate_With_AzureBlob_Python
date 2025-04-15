# Introduction

This project is a communication service between Azure SQL and Blob Storage container. The Products table in the database includes a column named image_url, where the Blob URL is stored. This URL is used to acess the image via a GET request and display it on the frontend screen.

## General Objective

The general objective is to integrate Azure SQL Database and Azure Blob Storage to support CRUD operations and enable data and image display on a web interface.

### Speficic Objectives

* Create a Azure Blob Storage: Craete a Blog Storage using Microsoft Azure;
* Create a SQL Database: Create a SQL Databae in Microsoft Azure and set it up with an associated SQL Server instance;
* Create Services Comunication: Create a service communication using python with azure-storage-blob library and pymssql library;
* Create Frontend Communication: Establish communication between the database and a web interface.