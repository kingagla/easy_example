# Połączenie z SQL

W pliku ``SQL/SQL_connection.py`` znajdziesz przykładowy kod do połączenia swojej bazy z Pythonem. 

Tworząc połączenie z Pythonem musisz zdefiniować kilka parametrów:
- host - nazwa Twojego "MySQL Connection" - u nas to był "localhost"
- database - nazwa bazy danych, czyli właściwe nazwa schema do którego chcesz się podłączyć
- user - nazwa użytkownika, domyślnie to zazwyczaj "root"
- password - hasło, które zdefiniowała_eś dla użytkownika w celu połączenia się z hostem.


**Pamiętaj, aby nie udostępniać na githubie nazwy użytkownika i hasła!**

Jak zatem opublikować kod zawierający połączenie do bazy bez publikowania takich danych? 
1. Stwórz plik o nazwie `.gitignore` - wszystko co zapiszesz w tym pliku będzie od teraz ignorowane przez 
   GIT - będziesz te pliki widzieć u siebie lokalnie, ale nie będą one częścią Twojego repozytorium i 
   nie będą wrzucane na serwer gdy robisz push
   
   1. Gdy chcesz wprowadzić do `.gitignore` plik, który już istnieje w repo, to zmieni on kolor na zielono-żółty. 
   Jeżeli jednak nie zmieni on koloru i nadal będzie w kolorze typowym dla plików będących w repo 
   (niebieski w przypadku plików edytowanych lub zielony w przypadku nowych plików), to musisz usunąć cache dla
   tego konkretnego pliku. Aby to zrobić otwórz terminal i wpisz w nim ``git rm --cached nazwa_pliku.py``
      
2. Zapisz w pliku `.gitignore` `settings.py`
3. Utwórz plik ``settings.py`` - jeżeli utworzysz go w jakimś pod-folderze, to pamiętaj aby nazwa pliku 
w `.gitignore` uwzględniała ścieżkę do niego (jeśli `settings.py` zapiszę w folderze `SQL`, to w `.gitignore`)
   muszę mieć zapisaną ścieżkę jako ``SQL/settings.py``
   
4. W pliku ``settings.py`` zapisz zmienne ``user`` i ``password`` nazwę usera ze swojego localhosta i hasło, 
które utworzyła_eś definiując localhosta.
   
5. Zaimportuj usera i hasło do pliku, w którym tworzysz połączenie. Pamiętaj, że importując odnosimy się do 
ścieżku do pliku zakładając, że root naszego projektu (podstawowy folder projektu) jest ścieżką domyślną, czyli 
   jeżeli utworzyłe_aś ``settings.py`` zapiszesz import jako ``from settings import user, password``, jeżeli 
   utworzyłe_aś to w folderze zapiszesz import jako ``from nazwa_folferu.settings import user, password``, np. 
   ``from SQL.settings import user, password``