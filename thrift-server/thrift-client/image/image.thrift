struct Image{
    1: binary blob,
}
service Service {
    string send(1: Image img),
}
