## Отчет по лаборатоной работе №2: Ручное построение нисходящих парсеров
### Разработка грамматики

Язык - Описание переменных в Си. Сначала идет имя типа, затем разделенные запятыми имена переменных. Должны поддерживаться указатели.

##### Грамматика:

    S -> LS
    S -> eps
    L -> nV;
    V -> V'N
    V' -> *V'
    V' -> n
    N -> ,V'N
    N -> eps

##### Описание нетерминалов:

    S - стартовый нетерминал. Генерирует L.
    L - описание типа и генерация V.
    V - описание переменных путем генерации V' и N
    V' - описание имени переменной, обработка указателей
    N - обработка терминала COMMA и обработка дальнейших переменных.
    
##### Описание терминалов:

    *   |   STAR
    ;   |   SEMICOLON
    n   |   NAME
    $   |   ENDFILE
    ,   |   COMMA
 

Можно увидеть, что грамматика не имеет *левой рекурсии*, значит, является `LL1` грамматикой, поэтому можно построить следующие множества.
##### Построение множеств `FIRST`, `FOLLOW`:
 
Нетерминал|First|Follow
|---------|-----|------|
S   |eps n|$
L   |n| eps n, $
V   |* n|;
V'  |* n|, ;
N   |, eps|;

##### Структура дерева
Количество табуляций - уровень вложенности. Вершины, имеющие одинаковый уровень вложенннсти, являются детьми вершины, имеющей уровень вложенноти на один меньший. Корень имеет уровень вложенности 0.

##### Описание тестов

Тест|Описание|
|--------|------------|
int a;|Тест на работоспособность
char *a|Тест на обработку указателей
long *b, ***a, c, d3;|Тест на обработку множества переменных
\t\t\t\\n  int *\r\t *bc, d\t\t  , ****d\n;|Тест на обработку whitespace'ов
