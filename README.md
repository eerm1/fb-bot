# fb-bot
Facebook-messenger бот для агрегации мемов с реддита.

Для создания бота нам понадобятся библиотеки flask, pymessenger, praw, поэтому, для начала установим их. Далее зарегистрируемся на фейсбуке и реддите и создадим аккаунты разработчика.
Далее создадим базовое flask приложение и будем превращать его в бота. Чтобы сделать бота, нам нужно уметь обрабатывать два типа запросов, GET и POST. Мы будем использовать запросы GET, когда Facebook veify token.
Для этого создадим функцию recieve_message.Если бот не получает запрос GET, он, вероятно, получает запрос POST, когда Facebook отправляет вашему боту сообщение, отправленное пользователем.
Далее создадим функцию verify_fb_token, проверяющую verify token и функцию send_message, которая отправляет сообщение пользователю. Так же создадим приложения в фейсбуке и реддите и возьмем оттуда всю нужную информацию и вставим в начало кода.
После этого установим local_tunnel, сгенерируем url и вставим его везде, где надо. Дальше создадим виртуальную машину, установим туда все необходимые пакеты и скопируем туда файл с кодом. Запустим бота оттуда(сервер localtunnel все равно падает, поэтому бот не хостится и приходится всегда запускать вручную)
Ссылка на страницу бота - https://www.facebook.com/Bot_test-437727210105825/?view_public_for=43772721010582
