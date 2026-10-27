Для создания презентации из md перейдите в папку с данным readme и выполните следующую команду:

```shell
pandoc -t beamer -V theme:Boadilla -V colortheme:dolphin inp.md --pdf-engine xelatex -V sansfont="Arial" -V fontsize=12pt -o out.pdf
```

Необходимо установить Pandoc.
Темы для оформления можно выбрать исходя из матрицы: https://hartwork.org/beamer-theme-matrix/
