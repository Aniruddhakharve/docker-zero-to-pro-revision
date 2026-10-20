# Lab: build-cache

```bash
docker build -t d31-cache:1.0 .
docker run --rm d31-cache:1.0
```

Then edit `app.py` and rebuild. Notice `pip install` layer is cached because `requirements.txt` did not change.
