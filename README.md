# Log Parser Pipeline

A modular Python-based ETL pipeline for ingesting, parsing, validating, transforming, and storing raw log data from multiple sources.

This project is designed as a hands-on data engineering practice project focused on building real-world pipeline architecture using Python.

## Project Goals
### Workflow

Raw Logs
   ↓
Ingestion
   ↓
Parsing
   ↓
Validation
   ↓
Transformation
   ↓
Storage
   ↓
Analytics / Reporting

### Features
Current Features
Read log files line-by-line efficiently
Parse multiple log formats
Structured output as Python dictionaries
Object-oriented parser architecture
Error handling for malformed logs
Modular pipeline design

### Planned Features
Validation layer
CSV export
SQLite storage
Metrics tracking
Pipeline logging
Real-time streaming support
Parallel processing
Analytics dashboard

Follow up will be creating a parsing strategy. 
the pipeline can determine whether the file is an apache log, json log or application log

Currently, the pipeline only works for application logs.

