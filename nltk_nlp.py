import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def main():
    try:
        sample_text = "Python is a wonderful programming language for machine learning and data science."
        print("Original Text:", sample_text)

        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt', quiet=True)
            nltk.download('punkt_tab', quiet=True)

        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords', quiet=True)

        tokens = word_tokenize(sample_text)
        print("\nWord Tokens:\n", tokens)

        stop_words = set(stopwords.words('english'))
        filtered_words = [w for w in tokens if w.lower() not in stop_words]
        print("\nFiltered Words (Stop Words Removed):\n", filtered_words)

    except ImportError:
        print("NLTK not installed. Run 'pip install nltk' to test NLTK features.")
    except Exception as e:
        print("NLTK note:", e)


if __name__ == "__main__":
    main()
