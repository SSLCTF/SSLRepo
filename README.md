# CTF Flag API

Простой API для получения флага.

---

## Base URL

```
http://tasks.sslctf.ru:8000/api/v1
```

---

## Авторизация

API использует **Bearer Token (JWT)** авторизацию.

### Заголовок:

```
Authorization: Bearer <your_jwt_token>
```

---

## Endpoint: Получение флага

### GET `/flag`

Возвращает флаг, если передан валидный токен.

---

### Request

**Headers:**

```
Authorization: Bearer <JWT>
```

---

### Response

**Status:** `200 OK`

```json
{
  "flag": "SSL_CTF{example_flag}"
}
```

---

### Возможные ошибки

| Код | Описание          |
| --- | ----------------- |
| 401 | Токен отсутствует |
| 403 | Невалидный токен  |

---

## Пример запроса

```bash
curl -X GET "http://tasks.sslctf.ru:8000/api/v1/flag" \
-H "Authorization: Bearer your_token_here"
```

https://github.com/SSLCTF/SSLRepo/