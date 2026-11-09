---
title: Docker для DevOps инженера. Практическое руководство.
author:
  - Михаил Долгих and Иван Евсеев
date: 26.11.04
header-includes: |
  \usepackage{fontawesome5}
theme_overrides:
  header:
    show: false
    text: ""
  footer:
    show: true
    text: "{title} Code and Cold Club 2026"
    show_slide_number: true
  toc:
    numbered: true
  colors:
    title_text: "#ffffff"
---
# Docker за час

Евсеев Иван Александрович 151319

Code and Cold Club 2026

---

## Оглавление

!toc

---

## Проблема

**Невозможность унификации рабочей системы и отсутствие автоматизации её развёртывания.**

- У каждого разработчика — своё окружение: версии ПО, библиотеки, настройки.
- «У меня работает» — не аргумент, если у коллеги не работает.
- Ручная настройка системы отнимает время и воспроизводится с ошибками.
- Нет единого способа быстро развернуть одинаковую среду на любой машине.

**Вопрос:** как решить проблему унификации и автоматизации развёртывания?


---

## Методы виртуализации

Решение есть — **виртуализация**.

На данный момент основных инструмента два:

1. **Виртуальные машины (VM)** — работа через гипервизор.
2. **Контейнеры (Docker)** — работа через движок, использующий ядро ОС напрямую.

---

## Виртуальные машины

**Как работает:** гипервизор полностью эмулирует работу компьютера с точки зрения ОС, на него ставится полноценная гостевая ОС.

```mermaid
---
config:
  theme: base
  themeVariables:
    primaryTextColor: "#000000"
    lineColor: "#333333"
    edgeLabelBackground: "#ffffff"
---
flowchart TB
    subgraph HW["Физическое оборудование (CPU, RAM, диск)"]
        HV["Гипервизор"]
    end

    subgraph VM1["Виртуальная машина 1"]
        GOS1["Гостевая ОС<br/>(полная)"] --> APP1["Приложение +<br/>зависимости"]
    end

    subgraph VM2["Виртуальная машина 2"]
        GOS2["Гостевая ОС<br/>(полная)"] --> APP2["Приложение +<br/>зависимости"]
    end

    HV --> VM1
    HV --> VM2

    HV -.->|"полная эмуляция<br/>работы компьютера"| GOS1
    HV -.->|"полная эмуляция<br/>работы компьютера"| GOS2
```
---

**Плюсы:**
  - Полная изоляция — своя ОС, своё ядро.
  - Хорошо подходит для тестирования и обучения.
  - Высокий уровень безопасности.

**Минусы:**
  - Требует много ресурсов (CPU, RAM, диск).
  - Плохо масштабируется — каждая VM «весит» как отдельный компьютер.
  - Долгий запуск.

---
## Контейнеры

**Как работает:** движок напрямую использует ядро хост-ОС без эмуляции, а операционные системы обрезаются до минимально работоспособного состояния.

```mermaid
---
config:
  theme: base
  themeVariables:
    stateLabelColor: "#000000"
    transitionLabelColor: "#000000"
    labelBackgroundColor: "#ffffff"
---
flowchart TB
    subgraph HW["Физическое оборудование (CPU, RAM, диск)"]
        HOS["Хост-ОС<br/>+ ядро"]
        ENG["Движок контейнеризации<br/>(Docker Engine)"]
    end

    subgraph C1["Контейнер 1"]
        B1["Минимальный образ<br/>(обрезанная ОС)"] --> A1["Приложение +<br/>зависимости"]
    end

    subgraph C2["Контейнер 2"]
        B2["Минимальный образ<br/>(обрезанная ОС)"] --> A2["Приложение +<br/>зависимости"]
    end

    HOS --> ENG
    ENG --> C1
    ENG --> C2

    B1 -.->|"напрямую использует<br/>ядро хост-ОС"| HOS
    B2 -.->|"напрямую использует<br/>ядро хост-ОС"| HOS
```
---

**Плюсы:**
  - Лёгкость и скорость запуска.
  - Отличное масштабирование — одной командой можно поднять множество работоспособных систем с относительно низкими затратами.
  - Единый образ — одинаковая среда везде.

**Минусы:**
  - Вопросы безопасности: работа с ядром напрямую.
  - Для Docker требуются root-права (или настройка rootless-режима).

---
## А что же такое Docker?

**Docker** — платформа контейнеризации, которая позволяет упаковать приложение со всеми зависимостями в единый образ и запускать его в изолированном контейнере на любой машине с Docker.

**Ключевые понятия:**
  - Образ (image) — шаблон с приложением и зависимостями.
  - Контейнер (container) — запущенный экземпляр образа.
  - Dockerfile — инструкция сборки образа.
  - Docker Compose — описание многоконтейнерного приложения.

---

```mermaid
---
config:
  theme: light
  themeVariables:
    stateLabelColor: "#000000"
    transitionLabelColor: "#000000"
    labelBackgroundColor: "#ffffff"
---
flowchart LR
    subgraph CLIENT["Клиент"]
        CLI["Docker CLI<br/>(команда docker)"]
    end

    subgraph HOST["Docker Host (хост-машина)"]
        DAEMON["Docker Daemon<br/>(dockerd)"]
        API["REST API"]
        IMG["Образы (Images)"]
        CONT["Контейнеры (Containers)"]
    end

    subgraph REGISTRY["Registry (Docker Hub / приватный)"]
        REPO["Репозитории образов"]
    end

    CLI --> API
    API --> DAEMON
    DAEMON --> IMG
    DAEMON --> CONT
    DAEMON --> REPO
```

---
## Жизненный цикл контейнера

**Основные команды и этапы:**
- docker pull — загрузить образ из реестра.
- docker run — создать и запустить контейнер.
- docker ps — список запущенных контейнеров.
- docker stop / docker start — остановить / запустить.
- docker rm — удалить контейнер.
- docker rmi — удалить образ.

---

```mermaid
---
config:
  theme: base
  themeVariables:
    stateLabelColor: "#000000"
    transitionLabelColor: "#000000"
    labelBackgroundColor: "#ffffff"
---
stateDiagram-v2
    [*] --> Created: docker create
    [*] --> Running: docker run
    Created --> Running: docker start
    Running --> Paused: docker pause
    Paused --> Running: docker unpause
    Running --> Stopped: docker stop
    Running --> Stopped: docker kill
    Stopped --> Running: docker start
    Stopped --> [*]: docker rm
    Running --> [*]: docker rm -f
```

---

## Какие есть настройки?
```bash
docker run -d --name myapp -p 8080:80 -v /data:/app/data -e ENV=prod myimage:latest
```

- `-d` — запуск в фоне (detached).  
- `--name` — имя контейнера.
- `-p 8080:80` — проброс порта хост:контейнер.
- `-v /data:/app/data` — монтирование тома.
- `-e ENV=prod` — переменная окружения.
- `myimage:latest` — образ и тег.

---
## Масштабирование

**Docker позволяет масштабировать приложение:**
  - Docker Compose: docker compose up --scale web=3 — поднять несколько экземпляров сервиса.
  - Swarm / Kubernetes — оркестрация контейнеров для продакшена.
  - Один образ — множество контейнеров с низкими затратами ресурсов.

---
## Синтаксис
<!-- layout:two-column -->
**Dockerfile** — инструкция сборки образа:
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

**Docker Compose** — описание сервисов:
```yaml
services:
  web:
    build: .
    ports:
      - "8080:80"
```
---
# Задания

---
##  L0

- Запустить готовый контейнер: docker run hello-world.
- Посмотреть список контейнеров и образов.

---

## L1

- Написать простой Dockerfile для своего приложения.
- Собрать образ: docker build -t myapp ..
- Запустить контейнер и проверить работу.

---
## L2* 

- Написать docker-compose.yml для приложения с базой данных.
- Запустить: docker compose up.
- Настроить переменные окружения и тома.

---

## Обратная связь

!poll[Выразите своё мнение, идеи и пожелания в форме обратной связи](https://forms.yandex.com/cloud/6aec89e04a052d3a210da82e) 

---

# Источники

- https://www.docker.com/resources/what-container
- https://docs.docker.com/compose/gettingstarted

