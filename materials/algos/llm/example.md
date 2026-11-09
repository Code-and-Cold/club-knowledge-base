---
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
theme: horizon
title: Обзор средств создания презентаций из MD
author: Степанов Николай Викторович
date: 2026.11.03
---
# Обзор средств создания презентаций из MD

Степанов Николай Викторович 151319

Code and Cold Club 2026

---

## Оглавление

!toc

---

## Мотивация

Создание презентаций через конвертацию из Markdown позволяет:

- Отделить содержание презентации от оформления.
- Применить развитые инструменты группового редактирования и версионирования текста.
- Автоматизировать множественный экспорт форматов.
- Уменьшить зависимость от конкретных продуктов MS.
- Снизить системные требования к оборудованию для создания презентаций.

---

## Сравнение существующих решений

![](assets/table.png)

---

<!-- hidden -->
## Сравнение существующих решений

|  | Pandoc plugins | Obsidian plugins | Marp | Kova | Slidev | Zettlr | Prezo |
|---|---|---|---|---|---|---|---|
| **Русский язык** | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ |
| **Лёгкость установки** | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Mermaid** | ⚠️ | ✅ | ⚠️ | ✅ | ✅ | ✅ | ❌ |
| **Экспорт** | PDF, HTML, PPTX, LaTeX, reveal.js, Beamer | HTML, PDF, PPTX | PDF, HTML, PPTX, PNG | PDF, PPTX, HTML | PDF, PNG, PPTX, SPA | PDF, DOCX, HTML | PDF, HTML, PNG, SVG |
| **Живой предпросмотр** | ⚠️ | ✅ | ✅ | ✅ | ✅ | ❌ | ⚠️ |
| **Заметки докладчика** | ⚠️ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| **Синтаксис MD** | Pandoc MD | Obsidian + Marp/reveal.js | Marp MD | Plain MD + GFM | Slidev MD (+Vue) | Pandoc/Zettlr MD | Marp/Deckset-подобный |
| **Лицензия** | FOSS (GPL) | FOSS (Obsidian — freemium) | FOSS (MIT) | FOSS (GPL-3.0 / MIT) | FOSS (MIT) | FOSS (GPL) | FOSS (MIT) |
| **Платформа** | Win / macOS / Linux / mobile | Win / macOS / Linux / mobile | Win / macOS / Linux | Win / macOS / Linux | Win / macOS / Linux | Win / macOS / Linux | Win / macOS / Linux |
| **Формат приложения** | CLI | GUI | GUI / CLI | GUI | CLI / Web | GUI | TUI |

---

# Демо инструментов

---

## Pandoc plugins

Pandoc поддерживает несколько плагинов для работы с презентациями, в частности для создания HTML, PDF и PPTX презентаций.

Для примера откроем презентацию, созданную через Pandoc + Beamer (Beamer конвертирует в PDF) для предыдущего занятия клуба.

---

## Obsidian plugins

Obsidian — это приложение для работы с заметками в формате MD с широкой экосистемой плагинов.

Существует несколько плагинов для интеграции Obsidian с системами создания презентаций, в том числе встроенный плагин Slides.

Наиболее популярный — Advanced Slides. Пример презентации: https://mszturc.github.io/obsidian-advanced-slides/examples/minml/#/

---

## Marp

Marp — это экосистема продуктов, специализирующаяся на создании презентаций из MD.

На следующем слайде представлено демо.

---

![](assets/marp-cli.gif)

---

## Kova

Kova — это простое FOSS-решение для создания презентаций из md. Данная презентация создана с помощью Kova.

Для примера откроем презентацию, представленную на официальном сайте Kova (локальный экспортированный файл).

---

## Slidev

Slidev — это продвинутый инструмент создания презентаций из MD + Vue-кода, используемый разработчиками.

[Демо](https://sli.dev/new).

---

## Zettlr

Zettlr — это FOSS-альтернатива Obsidian, направленная на исследовательскую деятельность и лучшую автоматизацию её процессов.

Использует reveal.js — популярный механизм создания презентаций из MD.

[Reveal.js](https://revealjs.com/).

---

## Prezo

Напоследок — нишевый инструмент для просмотра и редактирования презентаций в терминале: Prezo.
Лёгкий, подходит для простых презентаций.

![](assets/prezo.gif)

---

# Практикум

Создание презентации

---

## Задание

Выберите один из предложенных ниже инструментов и создайте с его помощью презентацию. Экспортируйте её в форматы HTML, PDF и PPTX (если поддерживается).

Choose one of the tools below and use it to create a presentation. Export it to HTML, PDF, and PPTX formats (if supported).

- Kova — проще
- Prezo
- Slidev ([online](https://sli.dev/new)) — сложнее

Темы презентаций и источники будут приложены, но вы свободны выбирать свои.<!-- step: 1 -->

Presentation topics and sources will be attached, but you are free to choose your own.<!-- step: 1 -->

Также выбирайте язык (RU/EN) по своему усмотрению — ведущий осуществит перевод в случае необходимости.<!-- step: 2 -->

Also, choose the language (RU/EN) at your discretion — the host will translate if necessary.<!-- step: 2 -->

---

## Мнение

- Что было самым сложным?
- Что оказалось проще чем предполагали?

---

## Вывод

- Использование markdown для создания презентаций оправдано, если необходимо работать в группе или ресурсы ограничены. Цена - время, потраченное на освоение нового инструмента.

---

## Обратная связь

!poll[Выразите своё мнение, идеи и пожелания в форме обратной связи](https://forms.yandex.com/cloud/6ae9b9171f1eb5715a7028d5)

---

## Источники

- https://www.termdock.com/en/blog/terminal-presentations-markdown-to-slides#the-stack-marp-cli--claude-code--git
