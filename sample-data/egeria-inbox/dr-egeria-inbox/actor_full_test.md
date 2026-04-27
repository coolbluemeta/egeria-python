# Actor Manager Test

This file tests the Actor Manager commands in Dr.Egeria.

## Create Organization
### Qualified Name
org-acme
### Display Name
ACME Corp
### Team Type
Enterprise

## Create Team
### Qualified Name
team-hr
### Display Name
HR
### Team Type
Department

## Create Team
### Qualified Name
team-recruitment
### Display Name
Recruitment Team
### Team Type
Sub-department

## Link Team Structure
### Super Team
team-hr
### Sub Team
team-recruitment

## Create Person
### Qualified Name
person-erin
### Display Name
Erin Employee
### Job Title
HR Specialist

## Create Person Role
### Qualified Name
role-hr-specialist
### Display Name
HR Specialist Role
### Headcount
5

## Link Person Role Appointment
### Person
person-erin
### Person Role
role-hr-specialist

## Create Team Role
### Qualified Name
TeamRole-Devops Tiger Team
### Display Name
DevOps Tiger Team
### Headcount
5

## Link Team Leader
### Team
team-hr
### Team Leader Role
person-erin
