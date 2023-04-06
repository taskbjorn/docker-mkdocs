# Quick reference

* Maintained by: [taskbjorn](https://github.com/taskbjorn)
* Official Git repository: [docker-mkdocs on GitHub](https://github.com/taskbjorn/docker-mkdocs)

# Supported tags and respective Dockerfile links

* [latest](build/latest/Dockerfile)

# What is `docker-mkdocs`?

![Logo](logo.png)

`docker-mkdocs` is a minimalist Docker container based on the official NGINX image to build and serve MkDocs static files.

# Running using Docker Compose

Clone this repository to a new folder:

```shell
git clone https://github.com/taskbjorn/docker-mkdocs.git
```

If the MkDocs source files are stored in a private repository, you must provide the access through a private SSH key. In the following, we will assume the private key is stored in a file `id_rsa.ospk` under the home folder of the active user. 

```shell
cp ~/id_rsa.ospk ./data/.ssh/
chmod 700 ./data/.ssh
chmod 600 ./data/.ssh/config ./data/.ssh/id_rsa.ospk
sudo chown root:root ./data/.ssh
```

> Note that the `.ssh` folder must be owned by `root` as the container is running under root!

Edit the `docker-compose.yml` file to mount the `.ssh` folder into the container:

```yaml
services:
  app:
    (...)
    environment:
      - "GIT_REPOSITORY=<your-repository>"
      - "GIT_EMAIL=<your-email>"
      - "GIT_USERNAME=<your-username>"
    volumes:
      - ./.ssh/:/root/.ssh
      - <your-path>:/repo
```

Run the compose stack:

```shell
docker-compose up -d
```

# License
 
This image is licensed under [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).

As it is often the case with Docker images, some of the software contained in this image (e.g. the base image, software included in the base image, etc.) may be covered under a different license.

Please remember it is your responsibility as the end-user to ensure that your use case complies with the licenses of all included software.