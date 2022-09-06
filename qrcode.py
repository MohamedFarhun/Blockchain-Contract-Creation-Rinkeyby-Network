{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNvhkUR6Nncude1yL1QjXmR",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/MohamedFarhun/Blockchain-Contract-Creation-RinkeybyNetwork/blob/master/qrcode.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AQ69EnpNr7iP",
        "outputId": "604ff617-0cc9-4f40-e627-cc70eafe68e4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: qrcode in /usr/local/lib/python3.7/dist-packages (7.3.1)\n"
          ]
        }
      ],
      "source": [
        "!pip install qrcode"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import qrcode as qr\n",
        "img=qr.make(\"https://infocryptos.netlify.app/\")\n",
        "img.save(\"infocrypto_app.png\")"
      ],
      "metadata": {
        "id": "sPJicxzpsAGH"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import qrcode\n",
        "from PIL import Image"
      ],
      "metadata": {
        "id": "TDOy2qMTsNkp"
      },
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)"
      ],
      "metadata": {
        "id": "sZ_Pq6rrtfb_"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "qr.add_data(\"https://infocryptos.netlify.app/\")"
      ],
      "metadata": {
        "id": "rlXjqNfUuKVj"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "qr.make(fit=True)\n",
        "img=qr.make_image(fill_color=\"red\",back_color=\"white\")"
      ],
      "metadata": {
        "id": "fqsGch_ruUqw"
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "img.save(\"infocrypto_app.png\")"
      ],
      "metadata": {
        "id": "rydc8vIivck4"
      },
      "execution_count": 18,
      "outputs": []
    }
  ]
}