# Połączenie z SQL

W pliku ``SQL/SQL_connection.py`` znajdziesz przykładowy kod do połączenia swojej bazy z Pythonem. 

Tworząc połączenie z Pythonem musisz zdefiniować kilka parametrów:
- host - nazwa Twojego "MySQL Connection" - u nas to był "localhost"
- database - nazwa bazy danych, czyli właściwe nazwa schema do którego chcesz się podłączyć
- user - nazwa użytkownika, domyślnie to zazwyczaj "root"
- password - hasło, które zdefiniowała_eś dla użytkownika w celu połączenia się z hostem.


**Pamiętaj, aby nie udostępniać na githubie nazwy użytkownika i hasła!**

Jak zatem opublikować kod zawierający połączenie do bazy bez publikowania takich danych? 
1. Stwórz plik o nazwie .gitignore - wszystko co zapiszesz w tym pliku będzie od teraz ignorowane przez 
   GIT - będziesz te pliki widzieć u siebie lokalnie, ale nie będą one częścią Twojego repozytorium i 
   nie będą wrzucane na serwer gdy robisz push