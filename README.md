[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## The assessment

Available in the following formats:

- [Markdown](dest/Application%20Assessment.md)
- [Excel](dest/Application%20Assessment.xlsx)
- [CSV](dest/Application%20Assessment.csv)

## Development

### Install

1. Make sure you are using the Python version specified in the `.python-version` file (or use [pyenv](https://github.com/pyenv/pyenv) for the automation)
2. Run `make install`

### Build

1. Run `make build`

### Test the Python code

1. Run `make py-test`

## [Licence](LICENSE)

# The Pragmatic checklist to assess an application

When you plan to modernize an application, there are several questions to ask yourself/your customer to apprehend when the modernization would bring value.

This is a draft of potential questions you should take into consideration when doing an assessment.
"
The Excel file can be downloaded [here](Application-Assessment.xlsx).

![The checklist](media/screenshot.png)

## Content

Here are the categories to assess

### Hardware Core Infra

- Virtualization
- Number of Servers for App hosting (except DB)
- CPU
- Memory
- Disks
- App Location Hosting
- OS
- Container Ready
- Other / Misc

### Network

- Network / Cloud virtual Network / Landing Zone
- Firewall, Load Balancer
- Private or public Internet Endpoints
- Other / Misc

### Infrastructure

- Identity Management for Internal users
- Identity Management for External users
- DNS
- Certificates
- Infra Monitoring
- Backup
- Other / Misc

### Data & AI

- RDBMS / NoSQL (Software vendor)
- Number of Servers
- SOA (Kafka, RabbitMQ, MQ Series)
- File Server (size)
- Cache
- Data Migration
- Lambda Architecture
- Analytics
- AI
- Other / Misc

### Software Specifications

- Programming Language (Front, Middle, Back, Mobile)
- Software Stack (MEAN, MERN, LAMP...)
- Monolith / Micro-Services
- Libraries, SDK, Runtimes
- Dependency on on-premises IS
- Dependency on external solutions or services (SaaS)
- OSS Dependencies
- 3rd party components
- libraries (+ associated Licensing model)
- Other / Misc

### Software Services

- DevOps / DevSecOps
- API Management
- Application Performance Monitoring
- Service Registry / Mesh

### Metrics

- #Total Users
- #Simultaneous users
- #RPS (Request per second)
- DB Size
- DB Increase
- Transactions / RPS
- Number of Messages, calls, requests/days/month/year
- Other / Misc

### Project Management

- Software methodology (DevOps, Agile, CMMI, SAFE…)
- Software Delivery model (N/A, online/SaaS, ISV Setup…)
- Expected release cycles (i.e. updates frequency)
- Update Management (continuous/online, disconnected…)
- Project Documentation (diagrams, technical specs…)Describes here the shared files
- Who builds the app?
- Who runs the app?
- Maintenance Ops / Operating Model
- Skilling Plan
- Other / Misc

