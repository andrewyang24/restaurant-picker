class Restaurant {
  String name = "";
  String url = "";

  Restaurant(this.name, this.url);

  Restaurant.fromJson(Map<String, dynamic> json) {
    name = json['title'];
    url = json['url'];
  }
}
