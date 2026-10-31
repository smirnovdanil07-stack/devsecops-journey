mkdir -p ~/devsecops/lab1 — создать папку.

cd ~/devsecops/lab1 — перейти в папку.

ls — посмотреть файлы (эл-эс, не is).

cat notes.txt — вывести содержимое.

find ~/devsecops -name "*.txt" — найти файлы.

ps aux --sort=-%mem | head -n 6 — посмотреть процессы по памяти.

echo "текст" >> notes.txt — добавить строку в файл.

Git:

git config --global user.name "Имя" — задать имя.

git config --global user.email "почта" — задать почту.

git init — инициализировать.

git branch -M main — переименовать ветку.

git add . — добавить всё в индекс.

git commit -m "комментарий" — сделать коммит.

git remote add origin <URL> — привязать репозиторий.

git push -u origin main — запушить.

SSH:

ssh-keygen -t ed25519 -C "почта" — сгенерировать ключ.

cat ~/.ssh/id_ed25519.pub — вывести ключ.

ssh -T git@github.com — проверить связь с GitHub.

ssh vboxuser@localhost -p 2222 — подключиться к виртуалке из Windows (записать отдельно, что это для проброса портов).
