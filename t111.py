import stripe
from school_registration_system import settings
stripe.api_key = settings.STRIPE_API_KEY

print(stripe.api_key,"478374834738947893748 ")

pro1=stripe.Product.create(name="Gold Special")
price1=stripe.Price.create(
  unit_amount=22500,
  currency="usd",
  recurring={"interval": "year"},
  product=pro1.id,
)
stripe.Customer.create(
  description="arpan",
)
# print(t1)
