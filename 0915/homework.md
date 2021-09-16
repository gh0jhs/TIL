# HomeWork

### 1. Django User Model

```python
class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
```



### 2. Create user by ModelForm

```python
from django.contrib.auth.forms import UserCreationForm
```



### 3. Django sessions

```python
(a) django_session
(b) sessionid
```

