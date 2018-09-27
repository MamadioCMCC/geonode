# GFDRR

## build

Clone `git@github.com:pvalsecc/SPCgeonode.git` and checkout the `gfdrr`
branch. In there, check the branch of geonode being installed in the
`Dockerfile`. Then, from the root of this clone:

```shell
TAG=rebase_2.8.x
docker-compose build
docker tag olivierdalang/spcgeonode:django-dev camptocamp/geonode_django:$TAG
docker tag olivierdalang/spcgeonode:geoserver-dev camptocamp/geonode_geoserver:$TAG
docker push camptocamp/geonode_django:$TAG
docker push camptocamp/geonode_geoserver:$TAG
```


## prepare deploy

Clone `git@github.com:camptocamp/terraform-geonode.git` and checkout
`wip_pvi`. Then run from this clone:

```shell
mkdir -p $HOME/.terraform.d/plugins
make install
```

## deploy on int

Go to terraform-geonode/rancher-environments/gfdrr-geonode-int and run:

```shell
terraform init
```
