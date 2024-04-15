terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentionals)
  project     = var.project
  region      = var.region
}

resource "google_storage_bucket" "collisions-bucket" {
  name          = var.gcp_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
resource "google_bigquery_dataset" "dataset" {
  dataset_id                  = "nyc_motor_vehicle_collisions"
  friendly_name               = "NYC Motor Vehicle Collisions"
  description                 = "NYC Motor Vehicle Collisions dataset"
  location                    = var.location
  default_table_expiration_ms = 2592000000

  labels = {
    env = "default"
  }
}