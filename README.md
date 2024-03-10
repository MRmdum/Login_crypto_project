# Login for Student Cryptographique project

Just a simple login handling the passwords using hash+salt then aead encryption <br />
We used Google tink lib: https://github.com/tink-crypto/tink/blob/master/docs/PYTHON-HOWTO.md <br />
and Bcrypt lib: https://github.com/pyca/bcrypt <br />
<br />
To run just build and run with docker: <br />
docker build -t image_name . <br />
docker run -it --name container_name image_name <br />
