from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('user', )
        fields = ('title','content','image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article', 'user')

# class ArticleForm(forms.ModelForm):
#     # 위젯 설정 2.
#     title = forms.CharField(
#         max_length=140, 
#         label='제목',
#         help_text='140자 이내로 작성바랍니다.',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': '제목을 입력바랍니다.'
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'placeholder': '내용을 입력바랍니다.'
#             }
#         )
#     )
#     class Meta:
#         model = Article
#         fields = '__all__'
        # fields = ('title', )
        # exclude = ('title', )
        # 위젯 설정 1.
        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #             'placeholder': '제목을 입력바랍니다.'
        #         }
        #     )
        # }

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=1, 
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': '제목을 입력바랍니다.'
#             }
#         )
#     )
#     content = forms.CharField(
#         # label 내용 수정
#         label='내용',
#         # Django form에서 HTML 속성 지정 -> widget
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'my-content',
#                 'placeholder': '내용을 입력바랍니다.',
#                 'rows': 5,
#                 'cols': 60
#             }
#         )
#     )