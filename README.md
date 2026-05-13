# Log Parser Pipeline

A modular Python-based ETL pipeline for ingesting, parsing, validating, transforming, and storing raw log data from multiple sources.

This project is designed as a independent project focused on building real-world pipeline architecture using Python.

## Project Goals
### Workflow

```
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
```

### Features
Current Features
- Read log files line-by-line efficiently
- Parse Application log formats
- Structured output as Python dictionaries
- Object-oriented parser architecture
- Error handling for malformed logs
- Modular pipeline design
- Validation layer
- SQLite storage

### Planned Features
- Parse other log formats (apache log, json log)
- Metrics tracking
- Pipeline logging
- Parallel processing
