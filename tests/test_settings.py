from config.settings import local, production


def test_settings_debug_mode():
    assert local.DEBUG
    assert not production.DEBUG


def test_settings_secret_key():
    assert isinstance(local.SECRET_KEY, str)
    assert isinstance(production.SECRET_KEY, str)


def test_settings_allowedhost():
    assert isinstance(local.ALLOWED_HOSTS, list)
    assert isinstance(production.ALLOWED_HOSTS, list)


def test_settings_cache():
    assert "default" in local.CACHES.keys()
    assert "default" in production.CACHES.keys()


def test_settings_installedapps():
    assert isinstance(local.INSTALLED_APPS, list)
    assert isinstance(production.INSTALLED_APPS, list)


def test_settings_middleware():
    assert isinstance(local.MIDDLEWARE, list)
    assert isinstance(production.MIDDLEWARE, list)


def test_settings_internalips():
    assert isinstance(local.INTERNAL_IPS, list)
