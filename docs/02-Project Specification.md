# Project Specifications

### Process 1 – CREATE

* In the Create process, the user fill out an HTML form to add information to the database.

### Process 2 – GET ALL

* In the Get All process, the system retrieves the data and display the  informations on the screen.

## Requirements

The tables below show the functional and non-functional requirements that define the project scope. To determine the priority of each requirements, apply a priorization technique in the last column of the table.  

As tabelas que se seguem apresentam os requisitos funcionais e não funcionais que detalham o escopo do projeto. Para determinar a prioridade de requisitos, aplicar uma técnica de priorização de requisitos e detalhar como a técnica foi aplicada.

### Functional Requirements

<table>
<tbody>
<tr align=center>
<td width="150px"><b>ID</b></td>
<td width="500px"><b>Requirement Description</b></td>
<td width="150px"><b>Priority</b></td>
</tr>
<tr>
<td>RF-001</td>
<td>Must perform a GET operation with the database</td>
<td>High</td>
</tr>
<tr>
<td>RF-002</td>
<td>Must perform a CREATE operation with the database</td>
<td>High</td>
</tr>
<tr>
<td>RF-003</td>
<td>Must save the image in Azure Blob during CREATE operation</td>
<td>High</td>
</tr>
<tr>
<td>RF-004</td>
<td>Must save the Blob URL in the database colum during CREATE operation</td>
<td>High</td>
</tr>
</tbody>
</table>

### Non-Functional Requirements

<table>
<tbody>
<tr align=center>
<td width="150px"><b>ID</b></td>
<td width="500px"><b>Requirement Description</b></td>
<td width="150px"><b>Priority</b></td>
</tr>
<tr>
<td>RNF-01</td>
<td>The system must ensure low-latency request handling</td>
<td>Medium</td>
</tr>
<tr>
<td>RNF-02</td>
<td>The service must enseure the most stable communication possible with Azure Cloud, at the lowest cost</td>
<td>Medium</td>
</tr>
<tr>
<td>RNF-03</td>
<td>The system must comply with the regulatoins established by the General Data Protection Law(LGPD)</td>
<td>High</td>
</tr>
</tbody>
</table>

## Restrictions

The project is restricted by the items prsented in the following table

<table>
<tbody>
<tr align=center>
<td width="150px"><b>ID</b></td>
<td width="500px"><b>Requirement Description</b></td>
</tr>
<tr>
<td>RE-01</td>
<td>The project must be delivered on the DIO website</td>
</tr>
<td>RE-02</td>
<td>The project must be developed in Python, with all communications integrated with Azure Cloud services</td>
</tr>
</tbody>
</table>

