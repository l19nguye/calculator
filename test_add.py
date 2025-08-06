from lambda_function import lambda_handler

def test_lambda():
    assert lambda_handler("david", None)['statusCode'] == 200