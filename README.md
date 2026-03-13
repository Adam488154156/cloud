# Déploiement Infrastructure Cloud avec Terraform sur Azure

Ce projet déploie automatiquement une infrastructure cloud sur Microsoft Azure avec Terraform. Il inclut une machine virtuelle Ubuntu avec une application Flask et un stockage Blob Azure.

## Technologies utilisées

- Terraform
- Microsoft Azure
- Python / Flask
- Ubuntu 22.04

## Infrastructure créée

- Groupe de ressources Azure
- Réseau virtuel + sous-réseau
- IP publique
- Pare-feu (NSG) avec règles SSH et Flask
- Machine virtuelle Ubuntu (Standard_B2ls_v2, France Central)
- Storage Account avec containers `images` et `logs`

## Prérequis

- Terraform installé
- Azure CLI installé
- Un compte Microsoft Azure actif

## Installation

**1. Cloner le dépôt**
```bash
git clone https://github.com/ton-compte/tp-azure-terraform
cd tp-azure-terraform
```

**2. Se connecter à Azure**
```bash
az login
```

**3. Initialiser Terraform**
```bash
terraform init
```

**4. Déployer l'infrastructure**
```bash
terraform apply
```

**5. Récupérer l'IP publique**
```bash
terraform output vm_public_ip
```

## Déployer l'application Flask

Se connecter à la VM en SSH :
```bash
ssh azureuser@<IP_PUBLIQUE>
```

Installer Flask et lancer l'application :
```bash
sudo apt update && sudo apt install -y python3 python3-pip
pip3 install flask
python3 app.py
```

L'application est accessible sur `http://<IP_PUBLIQUE>:5000`

## Endpoints de l'API

| Méthode | URL | Description |
|---------|-----|-------------|
| GET | / | Vérifier que l'API fonctionne |
| GET | /files | Lister les fichiers |
| POST | /files | Ajouter un fichier |
| DELETE | /files/<nom> | Supprimer un fichier |

## Détruire l'infrastructure

```bash
terraform destroy
```

## Structure du projet

```
tp-azure-terraform/
├── provider.tf      # Configuration du provider Azure
├── main.tf          # Ressources Azure
├── variables.tf     # Variables
├── outputs.tf       # Outputs (IP, URL...)
├── app.py           # Application Flask
└── README.md
```
