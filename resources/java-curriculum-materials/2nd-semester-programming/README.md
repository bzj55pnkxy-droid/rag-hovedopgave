# Java Curriculum Learning Materials - 2nd Semester

This directory contains 9 tutorial-style learning materials for the 2nd Semester Java Programming curriculum.

## Content Philosophy

- **80% Explanation**: Architecture, design patterns, "why" questions, integration context
- **20% Code Examples**: Focused, annotated, real-world Spring Boot patterns
- **Audience**: Intermediate Java students (completed 1st semester)
- **Style**: Architectural thinking, GRASP principles, oral exam preparation

## Key Differences from 1st Semester

| Aspect | 1st Semester | 2nd Semester |
|--------|--------------|--------------|
| Topics | 16 weekly topics | 9 integrated topics |
| Focus | Core Java fundamentals | Full-stack web development |
| Exam | Written/practical exam | Oral examination with project demo |
| Projects | Individual exercises | Team projects (Kailua, Ønskeskyen) |
| Technologies | Java SE | Spring Boot, MySQL, Thymeleaf, Azure |

## Topic Sequence

Materials build on each other sequentially:

### Phase 1: Foundation
1. `topic-adt-collections.md` - Abstract Data Types & Collections Framework

### Phase 2: Database Fundamentals
2. `topic-html-fundamentals.md` - HTML5 Fundamentals
3. `topic-sql-fundamentals.md` - SQL Fundamentals

### Phase 3: Advanced Database
4. `topic-sql-advanced.md` - Advanced SQL & Database Administration

### Phase 3-4: Integration
5. `topic-database-java-integration.md` - Database-Java Integration (JdbcTemplate, RowMapper)

### Phase 5: Web Development
6. `topic-spring-boot-fundamentals.md` - Spring Boot & Web Development Fundamentals ⚠️ HIGHEST EXAM WEIGHT

### Phase 6: Advanced Web
7. `topic-sessions-ioc-di.md` - Sessions, IoC & Dependency Injection

### Cross-cutting
8. `topic-grasp-design-principles.md` - GRASP Design Principles

### Phase 8: Capstone
9. `topic-javadoc-exam-prep.md` - JavaDoc & Exam Preparation

## Projects

### Kailua Car Rental (Phase 4)
- Database-driven console application
- Validates: ADT/Collections, SQL Fundamentals, SQL Advanced, Database-Java Integration

### Ønskeskyen Wishlist (Phase 7)
- Full-stack web application with Azure deployment
- Validates: All topics (full semester synthesis)

## How to Use

Students should read topics in order, as each builds on prior topics' concepts, terminology, and examples. Each topic includes a "For the Next Topic Agent" section documenting established terminology and patterns.

## Generation Details

Generated using: `thoughts/shared/handoffs/java-curriculum-2nd-semester-master-handoff.md`

Source materials:
- Topic definitions: `curriculum-extraction/2nd-semester-programming/topics/`
- Curriculum source: `reverse-enginereed-curriculums/2nd-semester-programming-curriculum-outline.md`
- Pedagogical context: `curriculum-extraction/2nd-semester-programming/phase-structure.yaml`
- Dependencies: `curriculum-extraction/2nd-semester-programming/topic-graph.yaml`
