# rest_api.py

Die Datei `rest_api.py` enthält Funktionen zum Registrieren und Einloggen eines Benutzers über eine RESTful-API.

### Funktionen

1. `register(json_data)`
   - Registriert einen neuen Benutzer über einen POST-Request.
   - Parameter:
     - `json_data` (dict): Die Registrierungsdaten des Benutzers im JSON-Format.
   - Rückgabewert:
     - `str`: Das Ergebnis des Registrierungsversuchs.

2. `login(data)`
   - Loggt einen Benutzer über einen POST-Request ein.
   - Parameter:
     - `data` (dict): Die Anmeldedaten, die Benutzername und Passwort enthalten.
   - Rückgabewert:
     - `tuple`: Ein Tupel, das den Zugriffstoken und die Benutzer-ID enthält, wenn die Anmeldung erfolgreich ist, andernfalls `None`.

3. `call_login()`
   - Diese Funktion zeigt, wie die `login()`-Funktion aufgerufen und das Ergebnis behandelt wird.
   - Sie verwendet fest codierte Anmeldedaten für den Test.
   - Bei erfolgreicher Anmeldung wird die Zugriffsdaten und die Meldung "eingeloggt mit user" ausgegeben.
   - Andernfalls wird das Ergebnis der Anmeldung ausgegeben.

4. `call_register()`
   - Diese Funktion zeigt, wie die `register()`-Funktion aufgerufen und das Ergebnis behandelt wird.
   - Sie versucht, einen neuen Testaccount zu registrieren.
   - Bei erfolgreicher Registrierung wird das Registrierungsergebnis ausgegeben.
   - Andernfalls wird das Ergebnis der Registrierung ausgegeben.

### Verwendung
Um die Funktionen in diesem Skript zu verwenden, können Sie die `call_login()`- und `call_register()`-Funktionen aufrufen.

Hinweis: Stellen Sie sicher, dass Sie die richtige URL für die RESTful-API in den Funktionen `register()` und `login()` verwenden. In diesem Fall ist die URL auf "https://nope-server.azurewebsites.net/api/auth/register" und "https://nope-server.azurewebsites.net/api/auth/login" festgelegt.



Um zum Hauptmenü zurückzukehren, klicken Sie [hier](../README.md).
