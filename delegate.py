from flask import jsonify


def getCloudTypes():
    cloudTypes = [
        {
            "type": "OpenStack",
        },
        {
            "type": "Kubernetes"
        },
        {
            "type": "Windriver"
        },
    ]
    return jsonify(cloudTypes);


def getServices():
    services = [
        {
            "service-id": "252df035-349d-43e3-b106-5e3c2a6c2545",
            "service_description": "vCPE",
            "resource-version": "1554189554096"
        },
        {
            "service-id": "f5728144-f4a2-4bf8-9f0e-4ee924235c42",
            "service_description": "vFW",
            "resource-version": "1554189553181"
        },
        {
            "service-id": "8ef4bb58-4c86-48ed-bb86-d463ac198848",
            "service_description": "vFWCL",
            "resource-version": "1554189553505"
        },
        {
            "service-id": "79b9f9cc-7582-47db-ac2f-6cab4637f493",
            "service_description": "gNB",
            "resource-version": "1554189554715"
        },
        {
            "service-id": "befcdeae-7cbf-4570-9a29-9c1397308268",
            "service_description": "vLB",
            "resource-version": "1554189553791"
        },
        {
            "service-id": "bf1cbc90-0091-40e0-95cd-d6dccf7a6d5f",
            "service_description": "vIMS",
            "resource-version": "1554189554384"
        }
    ]
    return jsonify(services)


def getCloudRegions():
    # skorzystać z GET /cloud-infrastructure/cloud-regions
    cloudRegions = [
        {
            "cloud-owner": "CloudOwner",
            "cloud-region-id": "RegionOne",
            "cloud-type": "SharedNode",
            "owner-defined-type": "OwnerType",
            "cloud-region-version": "v1",
            "cloud-zone": "CloudZone",
            "resource-version": "1554189551045",
            "relationship-list": {
                "relationship": [
                    {
                        "related-to": "complex",
                        "related-link": "/aai/v11/cloud-infrastructure/complexes/complex/clli1",
                        "relationship-data": [
                            {
                                "relationship-key": "complex.physical-location-id",
                                "relationship-value": "clli1"
                            }
                        ]
                    }
                ]
            }
        },
        {
            "cloud-owner": "CloudOwner",
            "cloud-region-id": "RegionTwo",
            "cloud-type": "openstack",
            "cloud-region-version": "pike",
            "identity-url": "http://msb-iag.onap:80/api/multicloud/v0/CloudOwner_RegionTwo/identity/v2.0/tokens",
            "cloud-zone": "CloudZone",
            "complex-name": "clli1",
            "resource-version": "1554890140624",
            "relationship-list": {
                "relationship": [
                    {
                        "related-to": "complex",
                        "related-link": "/aai/v11/cloud-infrastructure/complexes/complex/clli1",
                        "relationship-data": [
                            {
                                "relationship-key": "complex.physical-location-id",
                                "relationship-value": "clli1"
                            }
                        ]
                    }
                ]
            }
        }
    ]
    return jsonify(cloudRegions)
