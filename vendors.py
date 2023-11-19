class Vendors:
    class AppVendors:
        def __init__(self, name, contact_url, profile_url):
            self.name = name
            self.contact_url = contact_url
            self.profile_url = profile_url

    def get_vendors(self):
        vendors = [
            self.AppVendors(
                name="EGCTV",
                profile_url="https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F268533%2Fpexels-photo-268533.jpeg%3Fcs%3Dsrgb%26dl%3Dpexels-pixabay-268533.jpg%26fm%3Djpg&tbnid=nwiTKnJXTwcwcM&vet=12ahUKEwiUy5jgwtCCAxVxrCcCHSgXCIQQMygBegQIARBw..i&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fbeautiful%2F&docid=B51x0PBR9KNzvM&w=1920&h=1278&itg=1&q=images&ved=2ahUKEwiUy5jgwtCCAxVxrCcCHSgXCIQQMygBegQIARBw",
                contact_url="#"
            )
        ]

        return vendors


class TopEarners:
    class AppTopEarners:
        def __init__(self, name, money_made, profile_url):
            self.name = name
            self.money_made = money_made
            self.profile_url = profile_url

    def get_top_earners(self):
        top_earners = [
            self.AppTopEarners(
                name="EGCTV",
                money_made="₦100,000,000",
                profile_url=""
            )
        ]
        return top_earners