# Login for Student Cryptographique project

Just a simple login handling the paswwords using hash+salt then aead encryption
We used Google tink lib: https://github.com/tink-crypto/tink/blob/master/docs/PYTHON-HOWTO.md
and Bcrypt lib: https://github.com/pyca/bcrypt

To run just build and run with docker:
docker build -t image_name .
docker run -it --name container_name image_name
