from rest_framework import serializers
from .models import Loja, Produto


class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['id', 'nome', 'localizacao', 'bairro']


class ProdutoSerializer(serializers.ModelSerializer):
    loja = LojaSerializer(read_only=True)  # GET: retorna detalhes da loja
    loja_id = serializers.PrimaryKeyRelatedField(
        source='loja',
        queryset=Loja.objects.all(),
        required=False,
        allow_null=True,
        write_only=False
    )

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco', 'imagem', 'data_criacao', 'loja', 'loja_id']