# from ..models import CarBrand, CarModel


# def save_car_data(data):
#     result = []

#     for entry in data:
#         brand_name = entry.get("CarBrand")

#         # Create or get the CarBrand
#         brand, created = CarBrand.objects.get_or_create(name=brand_name)

#         # Initialize a count for the current brand's models
#         brand_count = 0

#         for model_data in entry.get("CarModel", []):
#             model_name = model_data.get("name")

#             # Check if the model already exists for this brand
#             if not CarModel.objects.filter(brand=brand, name=model_name).exists():
#                 # Create the CarModel if it does not exist
#                 CarModel.objects.create(brand=brand, name=model_name)
#                 brand_count += 1

#         # Append the result for this brand
#         result.append({"CarBrand": brand_name, "CarModelCount": brand_count})

#     # Return the result in JSON format
#     return result
