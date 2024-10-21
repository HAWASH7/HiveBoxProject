provider "aws" {
  region = "us-west-2"
}

resource "aws_eks_cluster" "example" {
  name     = "example-cluster"
  role_arn = "<EKS_ROLE_ARN>"

  vpc_config {
    subnet_ids = ["<SUBNET_ID_1>", "<SUBNET_ID_2>"]
  }
}
