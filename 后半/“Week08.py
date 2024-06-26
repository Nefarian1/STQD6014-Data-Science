{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "source": [
        "# Get the train performace xml file here: https://github.com/wesm/pydata-book/blob/3rd-edition/datasets/mta_perf/Performance_MNR.xml"
      ],
      "metadata": {
        "id": "LakI_W8tVugO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Week 08: <font color='red'>Data Loading and Storage</font>**"
      ],
      "metadata": {
        "id": "nMZC2_Rb-0ba"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### **For details of this Topic (Data Loading, Storage, and File Formats), please refer to the textbook: \"Python for Data Analysis\" by Wes McKinney: https://wesmckinney.com/book/**"
      ],
      "metadata": {
        "id": "dqylmKAeZK2N"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### **Mount to Google Drive**"
      ],
      "metadata": {
        "id": "xHctbU4tAAHo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Mount to Google Drive\n",
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y4Mwm9Mi_s6t",
        "outputId": "8b0eeb2e-0657-4765-fbdc-33d9e096ce41"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **This is my first Colab <font color='red'>notebook</font>**"
      ],
      "metadata": {
        "id": "o5aGKJxyuUoZ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Summation\n",
        "1 + 2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Op9xWt8puRIp",
        "outputId": "31ffe8d2-82e6-424f-af04-693fe30c6ff9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "3"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Import Pandas and NumPy library**\n"
      ],
      "metadata": {
        "id": "HsDnPu8hXGDj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Import the library\n",
        "import pandas as pd\n",
        "import numpy as np"
      ],
      "metadata": {
        "id": "2wp1UJCOgoB2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Reading and Writing Data in Text Format: <font color='red'>*.csv*</font> or <font color='red'>*.txt format*</font>**"
      ],
      "metadata": {
        "id": "tH1TnUtnb1Fe"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# csv is comma separated value"
      ],
      "metadata": {
        "id": "ZL6EOzCOvlcj"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 395
        },
        "id": "fSJVdX9Af-qr",
        "outputId": "8502fa93-6897-42ca-e6fe-61640f389ad4"
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-387e04b7-5e52-4fb0-97fe-ab2adee3036b\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-387e04b7-5e52-4fb0-97fe-ab2adee3036b\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-4-c9f552fa6e47>\u001b[0m in \u001b[0;36m<cell line: 4>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;31m# Upload ex1.csv to Google Drive\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mgoogle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcolab\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mfiles\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0mfiles\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupload\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/google/colab/files.py\u001b[0m in \u001b[0;36mupload\u001b[0;34m()\u001b[0m\n\u001b[1;32m     67\u001b[0m   \"\"\"\n\u001b[1;32m     68\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 69\u001b[0;31m   \u001b[0muploaded_files\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_upload_files\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmultiple\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     70\u001b[0m   \u001b[0;31m# Mapping from original filename to filename as saved locally.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     71\u001b[0m   \u001b[0mlocal_filenames\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mdict\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/google/colab/files.py\u001b[0m in \u001b[0;36m_upload_files\u001b[0;34m(multiple)\u001b[0m\n\u001b[1;32m    154\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    155\u001b[0m   \u001b[0;31m# First result is always an indication that the file picker has completed.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 156\u001b[0;31m   result = _output.eval_js(\n\u001b[0m\u001b[1;32m    157\u001b[0m       'google.colab._files._uploadFiles(\"{input_id}\", \"{output_id}\")'.format(\n\u001b[1;32m    158\u001b[0m           \u001b[0minput_id\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0minput_id\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moutput_id\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0moutput_id\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/google/colab/output/_js.py\u001b[0m in \u001b[0;36meval_js\u001b[0;34m(script, ignore_result, timeout_sec)\u001b[0m\n\u001b[1;32m     38\u001b[0m   \u001b[0;32mif\u001b[0m \u001b[0mignore_result\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     39\u001b[0m     \u001b[0;32mreturn\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 40\u001b[0;31m   \u001b[0;32mreturn\u001b[0m \u001b[0m_message\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_reply_from_input\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrequest_id\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtimeout_sec\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     41\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     42\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/google/colab/_message.py\u001b[0m in \u001b[0;36mread_reply_from_input\u001b[0;34m(message_id, timeout_sec)\u001b[0m\n\u001b[1;32m     94\u001b[0m     \u001b[0mreply\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_read_next_input_message\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     95\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mreply\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0m_NOT_READY\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mreply\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdict\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 96\u001b[0;31m       \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m0.025\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     97\u001b[0m       \u001b[0;32mcontinue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     98\u001b[0m     if (\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ],
      "source": [
        "# Download the ex1.csv file here: https://tinyurl.com/yheh3evw\n",
        "# Upload ex1.csv to Google Drive\n",
        "from google.colab import files\n",
        "files.upload()"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Check where is the ex1.csv file being uploaded\n",
        "# pwd -> \"present working directory\"\n",
        "!pwd"
      ],
      "metadata": {
        "id": "NiPXxtT0C_x5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# cat() function - read and output the ex1.csv content\n",
        "# cat() is called concatenate\n",
        "!cat /content/ex1.csv"
      ],
      "metadata": {
        "id": "nIBokXyFAMV5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Read the file using the read_table() function\n",
        "# Without specifying the delimter\n",
        "# There is an error message here\n",
        "df = pd.read_table('/content/ex1.csv')\n",
        "df"
      ],
      "metadata": {
        "id": "u4iYwjCug25c"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Specified the delimiter: csv\n",
        "# csv -> comma separated value\n",
        "pd.read_table('/content/ex1.csv', sep = ',')"
      ],
      "metadata": {
        "id": "cwvOZAnlg6z9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Read the ex1.csv file directly from github\n",
        "# Get it from this URL: https://tinyurl.com/yc39yfdj\n",
        "url = \"https://tinyurl.com/yc39yfdj\"\n",
        "\n",
        "# Read using the read_csv() function\n",
        "df = pd.read_csv(url)\n",
        "print(df.head(2))"
      ],
      "metadata": {
        "id": "JmOB1FAbyY_b"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# A file without header\n",
        "# Download and upload ex2.csv file here: https://tinyurl.com/9tajbupr\n",
        "from google.colab import files\n",
        "files.upload()"
      ],
      "metadata": {
        "id": "Cnbh3ZKDhPRQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Output the ex2.csv content using bash command\n",
        "# File without header\n",
        "!cat /content/ex2.csv"
      ],
      "metadata": {
        "id": "TZWjOb4PCziU"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Download ex2.csv raw data directly from GitHub\n",
        "# Using this URL: https://tinyurl.com/y4xd66my\n",
        "# ex2.csv does not have header\n",
        "# Python will assign column name automatically\n",
        "url = 'https://tinyurl.com/y4xd66my'\n",
        "df = pd.read_csv(url, header=None)\n",
        "df"
      ],
      "metadata": {
        "id": "S0vH9PAjAUma"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Specify the column names ourself\n",
        "# Use this URL: https://tinyurl.com/y4xd66my\n",
        "pd.read_csv(url, names=['irrfan', 'fruit', 'car', 'pet', 'place'])"
      ],
      "metadata": {
        "id": "6DJNnqBoh0rD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Set which specific column as the index\n",
        "# Index -> becomes rowname\n",
        "# \"names\" -> name of the columns\n",
        "# Use this URL: https://tinyurl.com/y4xd66my\n",
        "names=['a', 'book', 'cat', 'donkey', 'elephant']\n",
        "pd.read_csv(url, names = names, index_col = 'book')"
      ],
      "metadata": {
        "id": "9zJ1lO_riDAV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Masking in Python**\n",
        "* Masking comes up when we want to <font color='red'>***extract, modify, count***</font>, or otherwise <font color='red'>***manipulate values in an array***</font> based on some criterion.\n",
        "* For example, we might wish to\n",
        "    * **count all values greater than a certain value**, or\n",
        "    * **perhaps remove all outliers that are above some threshold**."
      ],
      "metadata": {
        "id": "kAOsf6ekQb7z"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Hierarchical index - multiple indexing\n",
        "# Multiple indexing -> multiple rownames\n",
        "# Download and upload csv_mindex.csv here: https://tinyurl.com/mshf9jw7\n",
        "from google.colab import files\n",
        "files.upload()"
      ],
      "metadata": {
        "id": "jgL94i9LiaP0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Output the content using bash command\n",
        "!cat /content/csv_mindex.csv"
      ],
      "metadata": {
        "id": "C_2ABTh9Fc0z"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Using hierrachical index or multiple indexing\n",
        "# Download the raw data for csv_mindex.csv here: https://tinyurl.com/3cwxrzdz\n",
        "parsed = pd.read_csv('https://tinyurl.com/3cwxrzdz',\n",
        "                     index_col = ['key1', 'key2', 'value1'])\n",
        "parsed"
      ],
      "metadata": {
        "id": "ng4cz1xcjLmx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Table without a fixed delimiter\n",
        "# Download and upload ex3.txt here: https://tinyurl.com/2s3cffvf\n",
        "from google.colab import files\n",
        "files.upload()"
      ],
      "metadata": {
        "id": "I7qykVZGjUPR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Output ex3.txt content using bash command\n",
        "!cat /content/ex3.txt"
      ],
      "metadata": {
        "id": "C963Hx-KI6uG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Dealing with data without fixed delimiter\n",
        "# sep='\\s+' denote one or more spaces.\n",
        "# Load the data using this URL: https://bit.ly/3YPjCtb\n",
        "res = pd.read_table('https://bit.ly/3YPjCtb',\n",
        "                    sep='\\s+')\n",
        "res"
      ],
      "metadata": {
        "id": "am4OXzFSnXpC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Files with comments embedded\n",
        "# Load ex4.csv here: https://tinyurl.com/mr4ex879\n",
        "# Using skip rows as parser function\n",
        "pd.read_table('https://tinyurl.com/mr4ex879',\n",
        "              skiprows = [0, 2, 3], sep = ',')"
      ],
      "metadata": {
        "id": "Mnzhx9dsp4y2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Another method: Use the \"comment\" function\n",
        "# URL: https://bit.ly/3HXjXUR\n",
        "pd.read_table('https://tinyurl.com/mr4ex879',\n",
        "              comment = '#', sep = ',')"
      ],
      "metadata": {
        "id": "f0ATu8hSFy8A"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **We want to deal with files with missing data**"
      ],
      "metadata": {
        "id": "mZyGT-5L7cUw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Download and upload ex5.csv here: https://tinyurl.com/7x8ehbda\n",
        "from google.colab import files\n",
        "files.upload()"
      ],
      "metadata": {
        "id": "KrB79_nFPrn_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Output ex5.csv content\n",
        "# Use notepad++ or excel to view\n",
        "!cat /content/ex5.csv"
      ],
      "metadata": {
        "id": "87cX8tlGRPoQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Files with missing values\n",
        "# Download ex5.csv here: https://tinyurl.com/yc4v35d6\n",
        "# Handle missing values - NaN (Not a Number)\n",
        "res = pd.read_csv('https://tinyurl.com/yc4v35d6', na_values=['NULL'])\n",
        "res"
      ],
      "metadata": {
        "id": "ju5WlyBJqZZT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Check the presence of null value - True of False\n",
        "pd.isnull(res)"
      ],
      "metadata": {
        "id": "E3Rsj_Htq9bK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Sentinels** are singleton objects that typically represent\n",
        "* some terminating (end) condition, or\n",
        "* **have a special, symbolic meaning**."
      ],
      "metadata": {
        "id": "MwuTaTVXfmSC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Specified sentinels - unique placeholder values\n",
        "# Get the raw data for ex5.csv here: https://tinyurl.com/yc4v35d6\n",
        "print(res)\n",
        "print(\"\\n------------------------------------\\n\")\n",
        "\n",
        "sentinels = {'message': ['foo', 'Na'], 'something': ['two']}\n",
        "pd.read_csv('https://tinyurl.com/yc4v35d6', na_values=sentinels)"
      ],
      "metadata": {
        "id": "aXGwmLwxrj-u"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Reading Text Files in Pieces**\n",
        "### When ***processing very large files***, we may want to read only a small piece of a file"
      ],
      "metadata": {
        "id": "4xTUgyWJUyAn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Change pandas display settings to become more compact\n",
        "# Setting the maximum number of rows to 6\n",
        "pd.options.display.max_rows=6"
      ],
      "metadata": {
        "id": "KeyRZP0msPXu"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Read a large csv file - display six rows\n",
        "# Download ex6.csv here: https://tinyurl.com/3dv6buw8\n",
        "# pd.options.display.max_rows=6\n",
        "res = pd.read_csv('https://tinyurl.com/3dv6buw8')\n",
        "res.head(15)"
      ],
      "metadata": {
        "id": "6J-InoVxtJmG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Only display a small number of rows\n",
        "pd.read_csv('https://tinyurl.com/3dv6buw8', nrows = 15)"
      ],
      "metadata": {
        "id": "Pu0YbUCXtUVe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Read ex5.csv: https://tinyurl.com/yc4v35d6\n",
        "dat = pd.read_csv('https://tinyurl.com/yc4v35d6')\n",
        "dat"
      ],
      "metadata": {
        "id": "Pi35Ldh_up7y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Write data\n",
        "dat.to_csv('/content/drive/MyDrive/STQD6014_Pxxxxx/diana.csv')"
      ],
      "metadata": {
        "id": "Z2dwW6sUvHZ6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Display output of the written file\n",
        "!cat /content/drive/MyDrive/STQD6014_Pxxxxx/diana.csv"
      ],
      "metadata": {
        "id": "Tpgzb6fWvPzc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Working with Other Delimited Formats**"
      ],
      "metadata": {
        "id": "D5IkNEVyXRpi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Other delimiters: using a pipe \"|\" or \"@\" or \"^\"\n",
        "# sys.stdout - prints the text result to the console instead of writing\n",
        "import sys\n",
        "dat.to_csv(sys.stdout, sep='@')"
      ],
      "metadata": {
        "id": "TtYfo886vfEh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Fill missing data with some string representation\n",
        "# na_rep: missing data representation\n",
        "dat.to_csv(sys.stdout, na_rep='@#$%')"
      ],
      "metadata": {
        "id": "AKk_ydLIvueD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Disable row and column label\n",
        "dat.to_csv(sys.stdout, index = False, header = False)"
      ],
      "metadata": {
        "id": "l5Pj1jZhwOja"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Write subset of the dataframe: a, b, c\n",
        "print(dat)\n",
        "print(\"\\n------------------------------------\\n\")\n",
        "\n",
        "dat.to_csv(sys.stdout, index = False, columns = ['a', 'b', 'c'])"
      ],
      "metadata": {
        "id": "2PE1zPy7wjcK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Pandas Series is a one-dimensional labeled array**\n",
        "* capable of holding data of any type\n",
        "    * <font color='red'>***integer, string, float, python objects***</font>, etc"
      ],
      "metadata": {
        "id": "XzSq4vzPHTTL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Pandas Series also has a to_csv method\n",
        "# Can incorporate NumPy function -> np.arange\n",
        "# np.arange returned an array range instead of list\n",
        "# This one has warning message!\n",
        "dates = pd.date_range('29/11/2023', periods = 7)\n",
        "ts = pd.Series(np.arange(7), index = dates)\n",
        "\n",
        "# Save it to your own folder\n",
        "ts.to_csv('/content/drive/MyDrive/STQD6014_Pxxxxx/tseries.csv')"
      ],
      "metadata": {
        "id": "hVuVokL1w4X4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# To find more information about pd.date_range\n",
        "?pd.date_range"
      ],
      "metadata": {
        "id": "jwXN8SvqCf0L"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Output the dates\n",
        "dates"
      ],
      "metadata": {
        "id": "n8_GW9FnB9df"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# To specify the exact date format\n",
        "date_string = '29/11/2023'\n",
        "date_format = '%d/%m/%Y'\n",
        "\n",
        "# Convert the date string to a datetime object\n",
        "start_date = pd.to_datetime(date_string, format = date_format)\n",
        "\n",
        "# Generate a date range with specified start date and periods\n",
        "date_range = pd.date_range(start_date, periods = 7)\n",
        "\n",
        "# Output the date range\n",
        "print(date_range)"
      ],
      "metadata": {
        "id": "qrjzlLLqDhV4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Starts November 1 (Tuesday), for seven periods; Week start on Tuesday\n",
        "dates = pd.date_range('11/1/2022', periods = 7, freq = ('W-WED'))\n",
        "dates"
      ],
      "metadata": {
        "id": "9QbYpRrMMHeo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Display dates content\n",
        "dates"
      ],
      "metadata": {
        "id": "fnQ8juEcxmfX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Display ts content\n",
        "ts"
      ],
      "metadata": {
        "id": "oM7U5UZRx3Kn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Display tseries.csv content\n",
        "!cat /content/drive/MyDrive/STQD6014_Pxxxxx/tseries.csv"
      ],
      "metadata": {
        "id": "sEgojMFWxVXi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **JSON Data format** - short for ***J***ava***S***cript ***O***bject ***N***otation\n",
        "1. one of the standard formats for sending data by HTTP request between web\n",
        "browsers and other applications\n",
        "2. much more free-form data format than a tabular text form like CSV\n",
        "3. basic types are objects (***dictionaries***), arrays (***lists***), strings, numbers, Booleans, and nulls.\n",
        "4. all of the ***keys*** in an object must be ***strings***"
      ],
      "metadata": {
        "id": "BirHwCXLW-Ig"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Python Lists**\n",
        "* **A list in a square bracket, [ ]**"
      ],
      "metadata": {
        "id": "jKQMb1EoMINW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Python Dictionary**\n",
        "* **A pair of curly bracket, { }**"
      ],
      "metadata": {
        "id": "VNoksrUyM3ep"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **The triple double quotes (\"\"\")**\n",
        "    * indicate a multiline string literal in Python.\n",
        "    * allows us to define a string that spans multiple lines."
      ],
      "metadata": {
        "id": "SKC9MPzkHTo6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Example of JSON data\n",
        "# When there is curly bracket -> either distionary or JSON\n",
        "# Because of triple quote -> this refers to JSON file\n",
        "# triple quote -> \"\"\" -> docstring\n",
        "obj = \"\"\"\n",
        "{\"name\": \"Wes\",\n",
        "  \"cities_lived\": [\"Akron\", \"Nashville\", \"New York\", \"San Francisco\"],\n",
        "  \"pet\": null,\n",
        "  \"siblings\": [{\"name\": \"Scott\", \"age\": 34, \"hobbies\": [\"guitars\", \"soccer\"]},\n",
        "               {\"name\": \"Katie\", \"age\": 42, \"hobbies\": [\"diving\", \"art\"]}]\n",
        "}\n",
        "\"\"\""
      ],
      "metadata": {
        "id": "qey-ltHc_aBB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Convert JSON string to Python form named res\n",
        "# 'res' would be a dictionary representing the parsed JSON data\n",
        "# this case it is a library\n",
        "import json\n",
        "res = json.loads(obj)\n",
        "res"
      ],
      "metadata": {
        "id": "4fXWLYYpC-1E"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Converts Python object back to JSON\n",
        "json.dumps(res)"
      ],
      "metadata": {
        "id": "OB1DSSIjDKVk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Convert JSON object to DataFrame\n",
        "siblings = pd.DataFrame(res[\"siblings\"], columns = ['name', 'hobbies'])\n",
        "siblings"
      ],
      "metadata": {
        "id": "AvyxfCJcDe3r"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Challenge: extract the city information and display in a dataframe\n",
        "pd.DataFrame(res[\"cities_lived\"], columns = ['CityInfo'])"
      ],
      "metadata": {
        "id": "ugaEhKg3ZGKM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **HTML file format**\n",
        "1. The pandas.read_html function by default searches for and attempts to parse all ***tabular data*** contained within ***\\<table>*** tags.\n",
        "2. The result is a ***list of DataFrame objects***"
      ],
      "metadata": {
        "id": "_oyoRq9nZyPg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Download data here: https://tinyurl.com/msaka5pd\n",
        "# The filename: fdic_failed_bank_list.html\n",
        "# fdic -> Federal Deposit Insurance Corporation\n",
        "# This is a list of banks which have failed since October 1, 2000.\n",
        "tbls = pd.read_html('https://tinyurl.com/msaka5pd')\n",
        "tbls"
      ],
      "metadata": {
        "id": "3mV8WvuxE9oV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# We only have one table\n",
        "# Check the length of the table\n",
        "len(tbls)"
      ],
      "metadata": {
        "id": "UE05JzCWRQ3H"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Output the content of the table\n",
        "failures = tbls[0]\n",
        "failures"
      ],
      "metadata": {
        "id": "BbUE2PiqF5R-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Perform data cleaning and analysis\n",
        "# Extract data from \"Closing Date\" column\n",
        "# Convert to standard date accepted internationally\n",
        "close_timestamps = pd.to_datetime(failures[\"Closing Date\"])\n",
        "close_timestamps"
      ],
      "metadata": {
        "id": "s9mjZLKaGJBC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Count frequency of banks closed for each year starting from Oct 1, 2000\n",
        "# dt -> DatetimeProperties\n",
        "close_timestamps.dt.year.value_counts()"
      ],
      "metadata": {
        "id": "okt3VZgGGgpq"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Parsing XML with lxml.objectify**\n",
        "1. parse the file and get a reference to the root node of the XML file with getroot, i.e. ***the document node***\n",
        "2. If we were describing a book using XML, for example, the root element might be **\\<book>** and everything related to that book—like **\\<title>**, **\\<author>**, and **\\<content>**—would be nested within it.\n",
        "\n",
        "3. The root element essentially provides the overall structure and context for the rest of the information in the XML document.\n",
        "\n",
        "# **Click here for more information about XML: https://tinyurl.com/3zdf4hab**"
      ],
      "metadata": {
        "id": "9pI2NMVkVdYF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Import XML library\n",
        "from lxml import objectify"
      ],
      "metadata": {
        "id": "tXdP_tEpGmDd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Download and upload Performance_MNR.xml file here: https://tinyurl.com/nh2kmn5z\n",
        "from google.colab import files\n",
        "files.upload()"
      ],
      "metadata": {
        "id": "CKLclCGrc1y3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Performance of train services published by The New York Metropolitan Transportation Authority (MTA)\n",
        "# Get the path of the Performance_MNR.xml file\n",
        "path = '/content/Performance_MNR.xml'\n",
        "\n",
        "# parses the contents of the file using objectify.parse()\n",
        "# parsing -> asking the computer to go through a file, find certain information, and make it ready for us to work with\n",
        "parsed = objectify.parse(open(path))\n",
        "root = parsed.getroot()"
      ],
      "metadata": {
        "id": "VuXIvp4PI0KH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# populate a dictionary of tag names to data values\n",
        "data = [] # Create an empty list\n",
        "\n",
        "skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ',\n",
        "               'DESIRED_CHANGE', 'DECIMAL_PLACES']\n",
        "\n",
        "# a for loop to access the information\n",
        "for elt in root.INDICATOR:\n",
        "    elt_data = {} # Create an empty dictionary\n",
        "    for child in elt.getchildren():\n",
        "        if child.tag in skip_fields:\n",
        "            continue\n",
        "        elt_data[child.tag] = child.pyval # the 'tag' is the key, the 'pyval' is the value\n",
        "    data.append(elt_data)"
      ],
      "metadata": {
        "id": "unNseUL2JrRD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Convert the list into a pandas DataFrame\n",
        "perf = pd.DataFrame(data)\n",
        "perf"
      ],
      "metadata": {
        "id": "gB_6WVTKKX7F"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Sneak peek of the DataFrame\n",
        "perf.head()"
      ],
      "metadata": {
        "id": "-VH-B5UmKcCA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Complete XML DataFrame\n",
        "perf2 = pd.read_xml(path)\n",
        "perf2.head()"
      ],
      "metadata": {
        "id": "KIQ_t76sKd3M"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Binary data files**\n",
        "\n",
        "# Binary file is not human-readable"
      ],
      "metadata": {
        "id": "cJxoq5A9ZGcC"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# CSV Data Formats\n",
        "frame = pd.read_csv('/content/ex1.csv')\n",
        "frame"
      ],
      "metadata": {
        "id": "uXOMZI3qLg5Q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Store data in binary format using Python's built-in pickle function\n",
        "frame.to_pickle('/content/frame_pickle')"
      ],
      "metadata": {
        "id": "3MsReNOIL88E"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# If you really want to see what the pickle file looked like\n",
        "!cat /content/frame_pickle"
      ],
      "metadata": {
        "id": "UU6sjzYtMWc3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# read pickle files\n",
        "pd.read_pickle('/content/frame_pickle')"
      ],
      "metadata": {
        "id": "SyFT8SsGMJ-y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Download the Parquet binary file: fec.parquet\n",
        "# Download data here: https://tinyurl.com/4t56bxjy\n",
        "from google.colab import files\n",
        "files.upload()"
      ],
      "metadata": {
        "id": "wOmjC8i1MVVB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Load the data\n",
        "fec = pd.read_parquet('/content/fec.parquet')\n",
        "fec"
      ],
      "metadata": {
        "id": "3Qx5_j0skPID"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Handling Microsoft excel files**"
      ],
      "metadata": {
        "id": "Afe_X62vbCQN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Download the ex1.xlsx here: https://tinyurl.com/359uwbk9\n",
        "xlsx = pd.ExcelFile(\"https://tinyurl.com/359uwbk9\")"
      ],
      "metadata": {
        "id": "KgLyeDVLN0cv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Getting excel sheet name\n",
        "xlsx.sheet_names"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wj78L25dObYs",
        "outputId": "d2a86bef-1558-430b-f45c-6b5cf45d354e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['Sheet1']"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Retrieve data by providing sheet name\n",
        "xlsx.parse(sheet_name = 'Sheet1')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 143
        },
        "id": "QCc_B9aZOj74",
        "outputId": "5eebea9a-c4bd-4004-c336-eec8b38794de"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Unnamed: 0  a   b   c   d message\n",
              "0           0  1   2   3   4   hello\n",
              "1           1  5   6   7   8   world\n",
              "2           2  9  10  11  12     foo"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-0c92c93e-6fce-4a08-b66e-3af78067b880\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Unnamed: 0</th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "      <th>d</th>\n",
              "      <th>message</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>3</td>\n",
              "      <td>4</td>\n",
              "      <td>hello</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>5</td>\n",
              "      <td>6</td>\n",
              "      <td>7</td>\n",
              "      <td>8</td>\n",
              "      <td>world</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2</td>\n",
              "      <td>9</td>\n",
              "      <td>10</td>\n",
              "      <td>11</td>\n",
              "      <td>12</td>\n",
              "      <td>foo</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-0c92c93e-6fce-4a08-b66e-3af78067b880')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-0c92c93e-6fce-4a08-b66e-3af78067b880 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-0c92c93e-6fce-4a08-b66e-3af78067b880');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-123572e5-2195-456b-be8e-8ed116018984\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-123572e5-2195-456b-be8e-8ed116018984')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-123572e5-2195-456b-be8e-8ed116018984 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Without index column\n",
        "xlsx.parse(sheet_name = 'Sheet1', index_col = 0)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 143
        },
        "id": "aw99pp2SOp85",
        "outputId": "c71df2a6-0e62-4d4d-93fd-7dbbd41b8a7a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   a   b   c   d message\n",
              "0  1   2   3   4   hello\n",
              "1  5   6   7   8   world\n",
              "2  9  10  11  12     foo"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-162eeb45-83fc-40ad-988c-953cbbdff692\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "      <th>d</th>\n",
              "      <th>message</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>3</td>\n",
              "      <td>4</td>\n",
              "      <td>hello</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>5</td>\n",
              "      <td>6</td>\n",
              "      <td>7</td>\n",
              "      <td>8</td>\n",
              "      <td>world</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>9</td>\n",
              "      <td>10</td>\n",
              "      <td>11</td>\n",
              "      <td>12</td>\n",
              "      <td>foo</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-162eeb45-83fc-40ad-988c-953cbbdff692')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-162eeb45-83fc-40ad-988c-953cbbdff692 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-162eeb45-83fc-40ad-988c-953cbbdff692');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-d002ad3b-0602-4308-9182-f5cb680ba86a\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-d002ad3b-0602-4308-9182-f5cb680ba86a')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-d002ad3b-0602-4308-9182-f5cb680ba86a button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Another way of reading the ex1.xlsx file\n",
        "frame = pd.read_excel('https://tinyurl.com/359uwbk9')\n",
        "frame"
      ],
      "metadata": {
        "id": "sQpyT5aeOznX",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 143
        },
        "outputId": "5692a446-3503-4ec1-8fc7-b14369cdeb4b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Unnamed: 0  a   b   c   d message\n",
              "0           0  1   2   3   4   hello\n",
              "1           1  5   6   7   8   world\n",
              "2           2  9  10  11  12     foo"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-9ad52f74-3d2a-4abf-8d25-1c5f5a59257e\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Unnamed: 0</th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "      <th>d</th>\n",
              "      <th>message</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>3</td>\n",
              "      <td>4</td>\n",
              "      <td>hello</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>5</td>\n",
              "      <td>6</td>\n",
              "      <td>7</td>\n",
              "      <td>8</td>\n",
              "      <td>world</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2</td>\n",
              "      <td>9</td>\n",
              "      <td>10</td>\n",
              "      <td>11</td>\n",
              "      <td>12</td>\n",
              "      <td>foo</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-9ad52f74-3d2a-4abf-8d25-1c5f5a59257e')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-9ad52f74-3d2a-4abf-8d25-1c5f5a59257e button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-9ad52f74-3d2a-4abf-8d25-1c5f5a59257e');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-e7d0109f-6f69-4cd3-9b41-fa03b5853147\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-e7d0109f-6f69-4cd3-9b41-fa03b5853147')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-e7d0109f-6f69-4cd3-9b41-fa03b5853147 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Write xlxs file\n",
        "# first create an ExcelWriter\n",
        "# This command cannot\n",
        "# Why?\n",
        "writer = pd.ExcelWriter(\"/content/ex2.xlsx\")"
      ],
      "metadata": {
        "id": "-SZWzzF8POVf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Output the frame content\n",
        "frame"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 143
        },
        "id": "P4BaLJqzZvBG",
        "outputId": "b6d8e1ad-e33e-489f-d207-4ee4052f8715"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   Unnamed: 0  a   b   c   d message\n",
              "0           0  1   2   3   4   hello\n",
              "1           1  5   6   7   8   world\n",
              "2           2  9  10  11  12     foo"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-95f9826f-ebdd-4536-aaed-82687fb9bb9d\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Unnamed: 0</th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "      <th>d</th>\n",
              "      <th>message</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>2</td>\n",
              "      <td>3</td>\n",
              "      <td>4</td>\n",
              "      <td>hello</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>5</td>\n",
              "      <td>6</td>\n",
              "      <td>7</td>\n",
              "      <td>8</td>\n",
              "      <td>world</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2</td>\n",
              "      <td>9</td>\n",
              "      <td>10</td>\n",
              "      <td>11</td>\n",
              "      <td>12</td>\n",
              "      <td>foo</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-95f9826f-ebdd-4536-aaed-82687fb9bb9d')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-95f9826f-ebdd-4536-aaed-82687fb9bb9d button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-95f9826f-ebdd-4536-aaed-82687fb9bb9d');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-7bd1c5e0-2733-4edb-bb46-bb0bda1cff67\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-7bd1c5e0-2733-4edb-bb46-bb0bda1cff67')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-7bd1c5e0-2733-4edb-bb46-bb0bda1cff67 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Provide a sheetname without ExcelWriter\n",
        "frame.to_excel(writer, \"Sheet1\")"
      ],
      "metadata": {
        "id": "YxBj3uesPba1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Another way\n",
        "# This one can?\n",
        "frame.to_excel(\"/content/ex222222.xlsx\")"
      ],
      "metadata": {
        "id": "IQMRzgwi02DO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Copy ex2.xlsx to a specific folder defined by you\n",
        "# using bash script\n",
        "!cp /content/ex2.xlsx /content/drive/MyDrive/STQD6014_ArusPerdana/_SEM1_20232024/Data"
      ],
      "metadata": {
        "id": "UlkFbSgyytQA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Interacting with HDF5 files**\n",
        "1. intended for storing large quantities of scientific array data.\n",
        "2. The ***“HDF”*** in HDF5 stands for ***h***ierarchical ***d***ata ***f***ormat.\n",
        "3. HDF5 file ***can store multiple datasets*** and ***supporting metadata***.\n",
        "4. HDF5 uses a structure similar to a **file directory**, where one can organize data within the file in various structured ways (just as with files stored on our computer).\n",
        "5. An HDF5 file can be described as the **definition of a file system** (folders, subfolders, and files stored in the computer) in a **single file**.\n",
        "\n",
        "### **Visit here for more information about HDF5: https://tinyurl.com/3a4nrskd**\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "_bXnUiFce-NA"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Working with HDF5\n",
        "# Create some random number\n",
        "np.random.seed(1213)\n",
        "frame = pd.DataFrame({\"a\": np.random.standard_normal(100)})\n",
        "frame"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "xNbbXuaDQNQ2",
        "outputId": "0b0b21c8-2463-4644-aa13-fef0fe4b0cfd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "           a\n",
              "0   0.511604\n",
              "1  -0.217660\n",
              "2  -0.521060\n",
              "3   1.253270\n",
              "4   1.104554\n",
              "..       ...\n",
              "95 -1.691711\n",
              "96  0.600202\n",
              "97  0.761825\n",
              "98 -1.156084\n",
              "99  1.875649\n",
              "\n",
              "[100 rows x 1 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-26ba98bd-d50b-40da-b87c-15bb4bbea8a1\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.511604</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>-0.217660</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>-0.521060</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1.253270</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1.104554</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>95</th>\n",
              "      <td>-1.691711</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>96</th>\n",
              "      <td>0.600202</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>97</th>\n",
              "      <td>0.761825</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>98</th>\n",
              "      <td>-1.156084</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>99</th>\n",
              "      <td>1.875649</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>100 rows × 1 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-26ba98bd-d50b-40da-b87c-15bb4bbea8a1')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-26ba98bd-d50b-40da-b87c-15bb4bbea8a1 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-26ba98bd-d50b-40da-b87c-15bb4bbea8a1');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-36323631-7fc0-402c-bb20-2b6305ef6c15\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-36323631-7fc0-402c-bb20-2b6305ef6c15')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-36323631-7fc0-402c-bb20-2b6305ef6c15 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Create a HDF5 file\n",
        "store = pd.HDFStore('/content/mydata.h5')"
      ],
      "metadata": {
        "id": "A0TO3F4kRg_T"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Put the data into the HDF5 file\n",
        "store[\"obj1\"] = frame"
      ],
      "metadata": {
        "id": "lxIyotI1RogS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Retrieve objects contained in the HDF5 file\n",
        "store[\"obj1\"]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "T2NiasmSdjbt",
        "outputId": "8def57ce-2aa1-4a63-a60a-21160897398f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "           a\n",
              "0   0.511604\n",
              "1  -0.217660\n",
              "2  -0.521060\n",
              "3   1.253270\n",
              "4   1.104554\n",
              "..       ...\n",
              "95 -1.691711\n",
              "96  0.600202\n",
              "97  0.761825\n",
              "98 -1.156084\n",
              "99  1.875649\n",
              "\n",
              "[100 rows x 1 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-42457b85-adc1-41cb-8a19-11fbefd993e0\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.511604</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>-0.217660</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>-0.521060</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1.253270</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1.104554</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>95</th>\n",
              "      <td>-1.691711</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>96</th>\n",
              "      <td>0.600202</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>97</th>\n",
              "      <td>0.761825</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>98</th>\n",
              "      <td>-1.156084</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>99</th>\n",
              "      <td>1.875649</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>100 rows × 1 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-42457b85-adc1-41cb-8a19-11fbefd993e0')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-42457b85-adc1-41cb-8a19-11fbefd993e0 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-42457b85-adc1-41cb-8a19-11fbefd993e0');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-ea1822de-8e6a-472c-a1bc-24925b4e5277\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-ea1822de-8e6a-472c-a1bc-24925b4e5277')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-ea1822de-8e6a-472c-a1bc-24925b4e5277 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# HDF5 support query operations in table storage format\n",
        "store.put('obj2', frame, format = 'table')\n",
        "print(store.select(\"obj2\", where = [\"index >= 1 and index <=4\"]))\n",
        "print('\\n -------- \\n')\n",
        "store.select(\"obj2\", where = [\"index >= 1 and index <=4\"]).mean()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pWDpMuehSUUq",
        "outputId": "8139d61b-1233-4d73-da6c-1174ad7c958c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "          a\n",
            "1 -0.217660\n",
            "2 -0.521060\n",
            "3  1.253270\n",
            "4  1.104554\n",
            "\n",
            " -------- \n",
            "\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "a    0.404776\n",
              "dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 39
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Other HDF functions\n",
        "frame.to_hdf('mydate.hdf5', 'obj3', format = 'table') # save the data into mydate.hdf5\n",
        "pd.read_hdf('mydate.hdf5', 'obj3', where = ['index < 5']) # Load the mydate.hdf5 file"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "ys258Tf2CZFW",
        "outputId": "5a60a4a1-17dd-47a3-d24e-e4a6b0ebb4a8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "          a\n",
              "0  0.511604\n",
              "1 -0.217660\n",
              "2 -0.521060\n",
              "3  1.253270\n",
              "4  1.104554"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-bce79346-05a3-435e-9940-c6e9132eea47\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0.511604</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>-0.217660</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>-0.521060</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1.253270</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1.104554</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-bce79346-05a3-435e-9940-c6e9132eea47')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-bce79346-05a3-435e-9940-c6e9132eea47 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-bce79346-05a3-435e-9940-c6e9132eea47');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-be94f6f3-4f97-4c4b-a38e-d25231909f90\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-be94f6f3-4f97-4c4b-a38e-d25231909f90')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-be94f6f3-4f97-4c4b-a38e-d25231909f90 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Interacting with Web APIs**\n",
        "1. Web API is a ***System to System interaction***, in which the ***data*** or information from one system ***can be accessed*** by another system, after the completion of execution the output is ***shown to the viewer***."
      ],
      "metadata": {
        "id": "pWmiFFbuC4p4"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### ***Task: To find the latest 30 GitHub issues for pandas on GitHub***"
      ],
      "metadata": {
        "id": "QFLeBmrM3VhG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# load library\n",
        "import requests"
      ],
      "metadata": {
        "id": "Dg-RlcwXTFd_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# first get the URL link: https://tinyurl.com/36ttfwsw\n",
        "url = 'https://tinyurl.com/36ttfwsw'"
      ],
      "metadata": {
        "id": "vnLmZEe3TUKi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Get the data\n",
        "resp = requests.get(url)"
      ],
      "metadata": {
        "id": "ks5vGzg2TbKX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **To undestand more on HTTP status, visit this link**: http://tinyurl.com/5cm2yhcw"
      ],
      "metadata": {
        "id": "Z0WT4kE75eGF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Check for the API status\n",
        "resp.raise_for_status()\n",
        "resp"
      ],
      "metadata": {
        "id": "CmPpRCSMTfHE",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "bea9cf01-2847-449f-d3de-e111c8ae5931"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Response [200]>"
            ]
          },
          "metadata": {},
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Return a dictionary containing JSON parsed into native Python objects:\n",
        "data = resp.json() # This is in json format"
      ],
      "metadata": {
        "id": "P_8pyobVTj2f"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Get the first data under title\n",
        "data[0][\"title\"]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 52
        },
        "id": "HwW1ezSATsvC",
        "outputId": "0031ba88-2cb7-48af-a98d-daec6921e790"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "\"BUG: `DataFrame.sort_index` is failing when `axis='columns'` and `ignore_index=True`\""
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 54
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Pass data directly to DataFrame and extract fields of interest:\n",
        "issues = pd.DataFrame(data, columns = ['id', 'number', 'title', 'labels', 'state'])\n",
        "issues"
      ],
      "metadata": {
        "id": "4535G3LWTv4u",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "outputId": "cef49855-06eb-4f4d-be2a-b067011a7164"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "            id  number                                              title  \\\n",
              "0   2038769351   56478  BUG: `DataFrame.sort_index` is failing when `a...   \n",
              "1   2038699234   56477            Create test_timestamp_fromisoformat.py    \n",
              "2   2038384925   56475  DOC: Add note about `git fetch upstream --tags...   \n",
              "3   2038258545   56474                      changes for spelling mistakes   \n",
              "4   2038216913   56473  DOC: Add example with ``numpy_nullable`` to ``...   \n",
              "5   2038188129   56471  DOC: Add example with ``numpy_nullable`` to ``...   \n",
              "6   2038169822   56470  DOC: Add example with ``numpy_nullable`` to ``...   \n",
              "7   2036865632   56466  Add optional parameter for pd.factorize to han...   \n",
              "8   2036610230   56463  BUG: Unsupported cast from string to time64 wi...   \n",
              "9   2036583595   56462  ENH:  Add a `cast` method to assist with typin...   \n",
              "10  2036386030   56460  BUG: bar a line plots are not aligned on the x...   \n",
              "11  2036310128   56459  BUG: Return numpy types from ArrowExtensionArr...   \n",
              "12  2035687149   56456  BUG: ChainedAssignmentError for CoW not workin...   \n",
              "13  2035546581   56455  BUG: dtype of right merge between datetime and...   \n",
              "14  2035524021   56454  BUG: left merge where right frame has differen...   \n",
              "15  2035255058   56452  BUG: sort_values() after multiple float operat...   \n",
              "16  2035140690   56451  BUG: Division over ExtensionArrays does not se...   \n",
              "17  2034857317   56448                       Fix/qcut multiple min values   \n",
              "18  2034707110   56447            ENH: Support case insensitive for merge   \n",
              "19  2034634149   56445           Adjust merge tests for new string option   \n",
              "20  2034585295   56442        BUG: merge not sorting for new string dtype   \n",
              "21  2034575282   56441  BUG: merge not raising for String and numeric ...   \n",
              "22  2034507395   56438      DEPS: Bump some code style check dependencies   \n",
              "23  2034506374   56437        TST: Test .groupby() encodes NaNs correctly   \n",
              "24  2034396592   56434                       BUG: Bug fix for spss kwargs   \n",
              "25  2034199458   56432               POC: Move some Tempita to Cython/C++   \n",
              "26  2034156071   56431                                      CLN: assorted   \n",
              "27  2034155666   56430  REF/EA-API: EA constructor without dtype speci...   \n",
              "28  2033787658   56425  BUG: Compatibility Issues of Numpy Methods wit...   \n",
              "29  2033407288   56419           BUG: setitem with mixed-resolution dt64s   \n",
              "\n",
              "                                               labels state  \n",
              "0   [{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...  open  \n",
              "1                                                  []  open  \n",
              "2   [{'id': 134699, 'node_id': 'MDU6TGFiZWwxMzQ2OT...  open  \n",
              "3                                                  []  open  \n",
              "4                                                  []  open  \n",
              "5                                                  []  open  \n",
              "6                                                  []  open  \n",
              "7                                                  []  open  \n",
              "8   [{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...  open  \n",
              "9   [{'id': 76812, 'node_id': 'MDU6TGFiZWw3NjgxMg=...  open  \n",
              "10  [{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...  open  \n",
              "11  [{'id': 49597148, 'node_id': 'MDU6TGFiZWw0OTU5...  open  \n",
              "12  [{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...  open  \n",
              "13  [{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...  open  \n",
              "14  [{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...  open  \n",
              "15  [{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...  open  \n",
              "16  [{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...  open  \n",
              "17                                                 []  open  \n",
              "18  [{'id': 76812, 'node_id': 'MDU6TGFiZWw3NjgxMg=...  open  \n",
              "19  [{'id': 57522093, 'node_id': 'MDU6TGFiZWw1NzUy...  open  \n",
              "20                                                 []  open  \n",
              "21  [{'id': 13098779, 'node_id': 'MDU6TGFiZWwxMzA5...  open  \n",
              "22  [{'id': 527603109, 'node_id': 'MDU6TGFiZWw1Mjc...  open  \n",
              "23                                                 []  open  \n",
              "24                                                 []  open  \n",
              "25                                                 []  open  \n",
              "26                                                 []  open  \n",
              "27  [{'id': 35818298, 'node_id': 'MDU6TGFiZWwzNTgx...  open  \n",
              "28                                                 []  open  \n",
              "29  [{'id': 2822098, 'node_id': 'MDU6TGFiZWwyODIyM...  open  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-9a7ee104-fa6a-4016-b6b9-84c4d18bc6c7\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>id</th>\n",
              "      <th>number</th>\n",
              "      <th>title</th>\n",
              "      <th>labels</th>\n",
              "      <th>state</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2038769351</td>\n",
              "      <td>56478</td>\n",
              "      <td>BUG: `DataFrame.sort_index` is failing when `a...</td>\n",
              "      <td>[{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2038699234</td>\n",
              "      <td>56477</td>\n",
              "      <td>Create test_timestamp_fromisoformat.py</td>\n",
              "      <td>[]</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2038384925</td>\n",
              "      <td>56475</td>\n",
              "      <td>DOC: Add note about `git fetch upstream --tags...</td>\n",
              "      <td>[{'id': 134699, 'node_id': 'MDU6TGFiZWwxMzQ2OT...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2038258545</td>\n",
              "      <td>56474</td>\n",
              "      <td>changes for spelling mistakes</td>\n",
              "      <td>[]</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2038216913</td>\n",
              "      <td>56473</td>\n",
              "      <td>DOC: Add example with ``numpy_nullable`` to ``...</td>\n",
              "      <td>[]</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>2038188129</td>\n",
              "      <td>56471</td>\n",
              "      <td>DOC: Add example with ``numpy_nullable`` to ``...</td>\n",
              "      <td>[]</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>2038169822</td>\n",
              "      <td>56470</td>\n",
              "      <td>DOC: Add example with ``numpy_nullable`` to ``...</td>\n",
              "      <td>[]</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>2036865632</td>\n",
              "      <td>56466</td>\n",
              "      <td>Add optional parameter for pd.factorize to han...</td>\n",
              "      <td>[]</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>2036610230</td>\n",
              "      <td>56463</td>\n",
              "      <td>BUG: Unsupported cast from string to time64 wi...</td>\n",
              "      <td>[{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>2036583595</td>\n",
              "      <td>56462</td>\n",
              "      <td>ENH:  Add a `cast` method to assist with typin...</td>\n",
              "      <td>[{'id': 76812, 'node_id': 'MDU6TGFiZWw3NjgxMg=...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>2036386030</td>\n",
              "      <td>56460</td>\n",
              "      <td>BUG: bar a line plots are not aligned on the x...</td>\n",
              "      <td>[{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>2036310128</td>\n",
              "      <td>56459</td>\n",
              "      <td>BUG: Return numpy types from ArrowExtensionArr...</td>\n",
              "      <td>[{'id': 49597148, 'node_id': 'MDU6TGFiZWw0OTU5...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>2035687149</td>\n",
              "      <td>56456</td>\n",
              "      <td>BUG: ChainedAssignmentError for CoW not workin...</td>\n",
              "      <td>[{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>2035546581</td>\n",
              "      <td>56455</td>\n",
              "      <td>BUG: dtype of right merge between datetime and...</td>\n",
              "      <td>[{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>2035524021</td>\n",
              "      <td>56454</td>\n",
              "      <td>BUG: left merge where right frame has differen...</td>\n",
              "      <td>[{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>2035255058</td>\n",
              "      <td>56452</td>\n",
              "      <td>BUG: sort_values() after multiple float operat...</td>\n",
              "      <td>[{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>2035140690</td>\n",
              "      <td>56451</td>\n",
              "      <td>BUG: Division over ExtensionArrays does not se...</td>\n",
              "      <td>[{'id': 76811, 'node_id': 'MDU6TGFiZWw3NjgxMQ=...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>17</th>\n",
              "      <td>2034857317</td>\n",
              "      <td>56448</td>\n",
              "      <td>Fix/qcut multiple min values</td>\n",
              "      <td>[]</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>18</th>\n",
              "      <td>2034707110</td>\n",
              "      <td>56447</td>\n",
              "      <td>ENH: Support case insensitive for merge</td>\n",
              "      <td>[{'id': 76812, 'node_id': 'MDU6TGFiZWw3NjgxMg=...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>19</th>\n",
              "      <td>2034634149</td>\n",
              "      <td>56445</td>\n",
              "      <td>Adjust merge tests for new string option</td>\n",
              "      <td>[{'id': 57522093, 'node_id': 'MDU6TGFiZWw1NzUy...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>20</th>\n",
              "      <td>2034585295</td>\n",
              "      <td>56442</td>\n",
              "      <td>BUG: merge not sorting for new string dtype</td>\n",
              "      <td>[]</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>21</th>\n",
              "      <td>2034575282</td>\n",
              "      <td>56441</td>\n",
              "      <td>BUG: merge not raising for String and numeric ...</td>\n",
              "      <td>[{'id': 13098779, 'node_id': 'MDU6TGFiZWwxMzA5...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>22</th>\n",
              "      <td>2034507395</td>\n",
              "      <td>56438</td>\n",
              "      <td>DEPS: Bump some code style check dependencies</td>\n",
              "      <td>[{'id': 527603109, 'node_id': 'MDU6TGFiZWw1Mjc...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>23</th>\n",
              "      <td>2034506374</td>\n",
              "      <td>56437</td>\n",
              "      <td>TST: Test .groupby() encodes NaNs correctly</td>\n",
              "      <td>[]</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>24</th>\n",
              "      <td>2034396592</td>\n",
              "      <td>56434</td>\n",
              "      <td>BUG: Bug fix for spss kwargs</td>\n",
              "      <td>[]</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25</th>\n",
              "      <td>2034199458</td>\n",
              "      <td>56432</td>\n",
              "      <td>POC: Move some Tempita to Cython/C++</td>\n",
              "      <td>[]</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>26</th>\n",
              "      <td>2034156071</td>\n",
              "      <td>56431</td>\n",
              "      <td>CLN: assorted</td>\n",
              "      <td>[]</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>27</th>\n",
              "      <td>2034155666</td>\n",
              "      <td>56430</td>\n",
              "      <td>REF/EA-API: EA constructor without dtype speci...</td>\n",
              "      <td>[{'id': 35818298, 'node_id': 'MDU6TGFiZWwzNTgx...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>28</th>\n",
              "      <td>2033787658</td>\n",
              "      <td>56425</td>\n",
              "      <td>BUG: Compatibility Issues of Numpy Methods wit...</td>\n",
              "      <td>[]</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>29</th>\n",
              "      <td>2033407288</td>\n",
              "      <td>56419</td>\n",
              "      <td>BUG: setitem with mixed-resolution dt64s</td>\n",
              "      <td>[{'id': 2822098, 'node_id': 'MDU6TGFiZWwyODIyM...</td>\n",
              "      <td>open</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-9a7ee104-fa6a-4016-b6b9-84c4d18bc6c7')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-9a7ee104-fa6a-4016-b6b9-84c4d18bc6c7 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-9a7ee104-fa6a-4016-b6b9-84c4d18bc6c7');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-1d23a3c9-201b-456c-9ac1-df7f726c2dc2\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-1d23a3c9-201b-456c-9ac1-df7f726c2dc2')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-1d23a3c9-201b-456c-9ac1-df7f726c2dc2 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 56
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Interacting with Databases - SQL**\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "OSv9uwjpDaGY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# SQL\n",
        "import sqlite3"
      ],
      "metadata": {
        "id": "zLk_9xyzUDe5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Create the SQL query\n",
        "# Define the structure and data type of the test table\n",
        "query = \"\"\"\n",
        "CREATE TABLE test\n",
        "(a VARCHAR(20), b VARCHAR(20),\n",
        "c REAL, d INTEGER\n",
        ");\"\"\""
      ],
      "metadata": {
        "id": "ShvmQqSqUlxW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# first create a SQLite3 database and connect to it\n",
        "con = sqlite3.connect('/content/mydata.sqlite')"
      ],
      "metadata": {
        "id": "WHy6wYxsU4di"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Execute the query\n",
        "con.execute(query)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ie1uSpW_VIJY",
        "outputId": "6c73e1a8-799e-47d1-9705-b0b8179b4359"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<sqlite3.Cursor at 0x7cb87242bf40>"
            ]
          },
          "metadata": {},
          "execution_count": 62
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Commit the query\n",
        "# Commit -> save the data\n",
        "con.commit()"
      ],
      "metadata": {
        "id": "1Dg_H8VIVK6J"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Create some data\n",
        "data = [(\"Atlanta\", \"Georgia\", 1.25, 6),\n",
        "        (\"Bangi\", \"Jalan Reko\", 3.3, 5),\n",
        "        (\"Seremban\", \"Nilai\", 5.5, 89)]"
      ],
      "metadata": {
        "id": "HbgZEPYRVN_c"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Create a query statement\n",
        "stmt = \"INSERT INTO test VALUES(?, ?, ?, ?)\""
      ],
      "metadata": {
        "id": "_GGrMSE-Vmi-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Execute\n",
        "con.executemany(stmt, data)"
      ],
      "metadata": {
        "id": "GmpEQGLfVuk9",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b1552e2d-2406-4e66-fe9c-47a5e0c56b67"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<sqlite3.Cursor at 0x7cb872311e40>"
            ]
          },
          "metadata": {},
          "execution_count": 67
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Commit -> save the data\n",
        "con.commit()"
      ],
      "metadata": {
        "id": "ZxoF_Mi9Vy8_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Python SQL drivers return a list of tuples when selecting data from a table\n",
        "# * -> everything\n",
        "# test -> table\n",
        "cursor = con.execute('select * from test')"
      ],
      "metadata": {
        "id": "CGGk0O9YV2mN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Fetch the data\n",
        "rows = cursor.fetchall()"
      ],
      "metadata": {
        "id": "9m4i8JRoV9xS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Print rows\n",
        "rows"
      ],
      "metadata": {
        "id": "4AGqNoizWAjH",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6ee37526-4547-4635-cf40-1df9d9580ce1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[('Atlanta', 'Georgia', 1.25, 6),\n",
              " ('Bangi', 'Jalan Reko', 3.3, 5),\n",
              " ('Seremban', 'Nilai', 5.5, 89)]"
            ]
          },
          "metadata": {},
          "execution_count": 72
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# cursor description only provides column names (the other fields, which are\n",
        "# part of Python’s Database API specification, are None)\n",
        "cursor.description"
      ],
      "metadata": {
        "id": "ESv0vYT6WBm1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fcedd762-960b-45ef-a50c-600cce0bed01"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(('a', None, None, None, None, None, None),\n",
              " ('b', None, None, None, None, None, None),\n",
              " ('c', None, None, None, None, None, None),\n",
              " ('d', None, None, None, None, None, None))"
            ]
          },
          "metadata": {},
          "execution_count": 73
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# We can pass the list of tuples to the DataFrame constructor,\n",
        "# but we also need the column names\n",
        "# Convert SQL Table to pandas Data Frame\n",
        "pd.DataFrame(rows, columns = [x[0] for x in cursor.description])"
      ],
      "metadata": {
        "id": "ivtkKa3jWJl4",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 143
        },
        "outputId": "db70553c-41bf-4ce4-f740-a37d24638060"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "          a           b     c   d\n",
              "0   Atlanta     Georgia  1.25   6\n",
              "1     Bangi  Jalan Reko  3.30   5\n",
              "2  Seremban       Nilai  5.50  89"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-9ba88f65-34d3-4a40-b2ed-8a49d6d9101f\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>a</th>\n",
              "      <th>b</th>\n",
              "      <th>c</th>\n",
              "      <th>d</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Atlanta</td>\n",
              "      <td>Georgia</td>\n",
              "      <td>1.25</td>\n",
              "      <td>6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Bangi</td>\n",
              "      <td>Jalan Reko</td>\n",
              "      <td>3.30</td>\n",
              "      <td>5</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Seremban</td>\n",
              "      <td>Nilai</td>\n",
              "      <td>5.50</td>\n",
              "      <td>89</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-9ba88f65-34d3-4a40-b2ed-8a49d6d9101f')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-9ba88f65-34d3-4a40-b2ed-8a49d6d9101f button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-9ba88f65-34d3-4a40-b2ed-8a49d6d9101f');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-560e9267-4bb8-4c92-8b1d-478167f51428\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-560e9267-4bb8-4c92-8b1d-478167f51428')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-560e9267-4bb8-4c92-8b1d-478167f51428 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 74
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Done for the day. Happy Mid-sem Break!!!**"
      ],
      "metadata": {
        "id": "PTEhuEiH5tK9"
      }
    }
  ]
}