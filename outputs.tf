output "vm_public_ip" {
  value = azurerm_public_ip.main.ip_address
}

output "flask_app_url" {
  value = "http://${azurerm_public_ip.main.ip_address}:5000"
}

output "storage_account_name" {
  value = azurerm_storage_account.main.name
}