from django import forms


class DummyForm(forms.Form):
    text = forms.CharField(label='Отзыв', min_length=3, max_length=10)
    grade = forms.IntegerField(label='Оценка', min_value=1, max_value=100)
    image = forms.FileField(label='Фотография', required=False)  # , required=False - поле не обязательным к заполнению

    # def clean_text(self):
    #     if "abc" not in self.cleaned_data['text']:  # валидация поля по содержимому
    #         raise forms.ValidationError('Вы не о том пишите')
