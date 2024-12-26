from fastapi import FastAPI


app = FastAPI()


secret = "some_secret_to_return"
@app.get("/secret")
def get_secret():

    return secret

"""

ALTER table_name("column_1",)



"""

