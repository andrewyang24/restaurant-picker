import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(primarySwatch: Colors.red),
      home: const RootPage(),
    );
  }
}

class RootPage extends StatefulWidget {
  const RootPage({Key? key}) : super(key: key);

  @override
  State<RootPage> createState() => _RootPageState();
}

class _RootPageState extends State<RootPage> {
  int currentPage = 0;

  String restaurantsdata = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Restaurant Picker'),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Text(restaurantsdata,
              style: const TextStyle(fontSize: 24, fontWeight: FontWeight.bold))
        ],
      ),
      floatingActionButton: FloatingActionButton(
          onPressed: () async {
            final response =
                await http.get(Uri.parse('http://127.0.0.1:5000/'));

            final decoded = json.decode(response.body) as Map<String, dynamic>;

            setState(() {
              restaurantsdata = decoded['greetings'];
            });
          },
          child: const Icon(Icons.add_business)),
    );
  }
}
