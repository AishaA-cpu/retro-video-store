from flask import Blueprint, jsonify, make_response, request
import requests
from app import db
from app.models.customer import Customer
from app.models.video import Video
from app.models.rental import Rental
from http import HTTPStatus
from datetime import date, datetime
from app.models.models_helps import model_helpers

customer_bp = Blueprint("customer_bp", __name__, url_prefix= "/customers")
video_bp = Blueprint("video_bp", __name__, url_prefix= "/videos")

@customer_bp.route("", methods=["GET"])
def get_all_customers():
    request_body = request.get_json()
    response_body = []
    customers = Customer.query.all()


    for customer in customers:
        response_body.append(
            {
                "id" : customer.id,
                "name": customer.name,
                "phone": customer.phone,
                "postal_code": customer.postal_code
            }
        )

    return jsonify(response_body)

@customer_bp.route("/<customer_id>", methods=["GET"])
def get_one_customer(customer_id):
    request_body = request.get_json()
    response_body = {}
    if not customer_id.isnumeric():
        return "", HTTPStatus.BAD_REQUEST

    customers = Customer.query.get(customer_id)
    
    if customers is None:
        return {
            "message":f"Customer {customer_id} was not found"
        }, HTTPStatus.NOT_FOUND

    response_body["id"] = customers.id
    response_body["name"] = customers.name
    response_body["phone"] = customers.phone
    response_body["postal_code"]= customers.postal_code

    return response_body, HTTPStatus.OK

@customer_bp.route("", methods=["POST"])
def post_one_customer():
    required_attributes = {"postal_code", "name", "phone"}
    response_body = {}

    form_data = request.get_json()
    attributes = set(form_data.keys())
    
    helpers = model_helpers()
    missing_attributes = helpers.missing_requirements(required_attributes, attributes)
    
    if missing_attributes:
        return {
            "details" : f"Request body must include {missing_attributes}."
        }, HTTPStatus.BAD_REQUEST
    
    new_customer = Customer (
        name = form_data["name"],
        phone  = form_data["phone"],
        registered_at = date.today(),
        postal_code = form_data["postal_code"]
    )

    db.session.add(new_customer)
    db.session.commit()

    #response_body["id"] = new_customer.id
    return {
        "id" : new_customer.id,
        "message" : f"customer {new_customer.id} successfully created"
    }, HTTPStatus.CREATED

    #return response_body, HTTPStatus.CREATED





@customer_bp.route("/<customer_id>", methods=["DELETE"])
def delete_one_customer(customer_id):
    request_body = request.get_json()
    response = {}

    customer = Customer.query.get(customer_id)
    if customer is None:
        return {
            "message": f"Customer {customer_id} was not found"
            }, HTTPStatus.NOT_FOUND

    db.session.delete(customer)
    db.session.commit()

    return {
        "id" : customer.id,
        "message" : f"customer {customer.id} successfully deleted"
    }, HTTPStatus.OK


@customer_bp.route("/<customer_id>", methods=["PUT"])
def update_one_customer(customer_id):
    form_data = request.get_json()
    response = {}
    required_attributes = {"postal_code", "name", "phone"}

    customer = Customer.query.get(customer_id)

    attributes = set(form_data.keys())

    if customer is None:
        return {
            "message": f"Customer {customer_id} was not found"
            }, HTTPStatus.NOT_FOUND

    helpers = model_helpers()
    missing_attributes = helpers.missing_requirements(required_attributes, attributes)
    
    if missing_attributes:
        return {
            "details" : f"Request body must include {missing_attributes}."
        }, HTTPStatus.BAD_REQUEST

    customer.name = form_data["name"],
    customer.phone = form_data["phone"],
    customer.postal_code = form_data["postal_code"]

    db.session.commit()

    return {
        "name" : customer.name,
        "phone": customer.phone,
        "postal_code": customer.postal_code
    }, HTTPStatus.OK






# ********************** videos
@video_bp.route("", methods=["POST"])
def post_one_video():
    pass

@video_bp.route("", methods=["GET"])
def get_all_videos():
    pass

@video_bp.route("/<video_id>", methods=["GET"])
def get_one_videos():
    pass

@video_bp.route("/<video_id>", methods=["PUT"])
def update_one_video():
    pass


@video_bp.route("/<video_id>", methods=["DELETE"])
def delete_one_videos():
    pass



