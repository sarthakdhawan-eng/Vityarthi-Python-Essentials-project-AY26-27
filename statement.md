# Project Statement - Flow

## Problem Statement

Students often keep study work in different notes and struggle to decide what to do first. A simple task list records the work but does not give a clear order. Flow solves this small problem using basic programming and algorithmic thinking.

## Scope

The project covers task creation, task viewing, completion, deletion, simple priority calculation, study-plan generation, and progress analysis. Data is kept in memory during one program run.

The project does not include a database, web application, API, machine learning model, login system, or external service.

## Target Users

- College students
- Students managing work from multiple subjects

## High-Level Features

- Add and view study tasks
- Mark tasks completed
- Delete tasks
- Generate a ranked study plan
- View completion statistics
- Load demo tasks

## Inputs

- Task title
- Subject
- Deadline
- Priority (1-5)
- Estimated study hours
- Task ID for completion/deletion

## Outputs

- Task list
- Ranked study plan
- Progress percentage
- Pending study hours
- Subject-wise task counts

## Core Workflow

```text
Start
  -> Show menu
  -> Read user choice
  -> Perform selected module
  -> Display result
  -> Return to menu
  -> Exit when user selects 0
```
