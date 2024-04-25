class Media:
    def media(a, b):
        return (a + b)/2

class Test_Media:
    def teste_media(self):
        result = Media.media(4, 4)
        assert result == 4

    def teste_media2(self):
        result = Media.media(8, 2)
        assert result == 5

    def teste_media3(self):
        result = Media.media(0, 10)
        assert result == 5

    def teste_media4(self):
        result = Media.media(5, 4)
        assert result == 4.5