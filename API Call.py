import requests

# API endpoint
url = "https://www.robotevents.com/api/v2/events"

# Your API key
api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiZmExNTlkODcwYWRiZTU2MGNmMzQwNTU2ZmRmN2JiMjRmNjgwZWQ3ZDg5YWE5ZTdiZjQxMDNhMTZlZTBlNmNkODFkZDZiNDNkODJmYmNiYTYiLCJpYXQiOjE3MzY1MTcwOTIuMjcxNTA1MSwibmJmIjoxNzM2NTE3MDkyLjI3MTUwOCwiZXhwIjoyNjgzMjAxODkyLjI2NDk4Nywic3ViIjoiMTQyNTkwIiwic2NvcGVzIjpbXX0.lda8sp5OZ4ArofulBB13K-0638X0A2EyGAz8yAt6TG3pd-2Z9KxZH_xXv5ZMaEkeUAOiGp69NSlZznWqgiig49JIVlGVuSSqklHPxNlzlr8wEOu1nA8cW-iZdrUv2FRt-gj_TYaD1am1VxXGJA-K3AYqlK-16tgWBlCPrfOs3MiiGduPJPa0QEMvy5XPaGLTLViwuzHKMIQWD60qKwZakzbx7x5rWlluCwBoXcu6X7IbdmFgFiUeEqyBCs3JbIn52aEaWS9i7488WHGjhRmUSM-BB_odLVWAoVAYwJEajPO-jl820cFqm57Ul08gfUspGrPCsP2iW59OJhm2seMfPhkkOHH08YG_vhrRnN-xVnDy82MlVC3x0cvr6JyVk9AK49NbVhgw9C30V2S5wNrZnvJSrqVlql2L3yhufEvkJBkjIxWWC4Fw-idOvEezjCIoJ9ISf-Dd-gDIVLH3FDLSWMbLWEnV_dBmw25mM-zJUepA1eCACnlJdl0YgnVw6FeI7plsicpa3x7NG70MW_vB9CX9qLOIF8sQw3xX94Dnbwgq3XcUeCJ8geCSISCu4gr2SKz4PKk1hkumlUMHQvHISeKPDj7WsCmrb8l_CvWCSA3e13_Zp2iTTfx-Cq-NLUc6xYrm4AQ6ZnlADRcWllGI483uj-nTjNZWFOp1imOeSlo"

# Headers with the API key
headers = {
    "Authorization": f"Bearer {api_key}",  # or "API-Key": api_key depending on API
    "Content-Type": "application/json"
}

# Make the request
response = requests.get(url, headers=headers)

# Check response
if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")
