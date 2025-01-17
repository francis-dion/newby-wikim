from typing import List, Optional
from datetime import datetime
from protection import Protection
from version import Version, PreviousVersion
from namespace import Namespace
from language import Language
from entity import Entity
from articlebody import ArticleBody
from license import License
from visibility import Visibility
from event import Event
from project import Project


class Image:
    def __init__(self,
                 content_url: Optional[str] = None,
                 width: Optional[int] = None,
                 height: Optional[int] = None,
                 alternative_text: Optional[str] = None,
                 caption: Optional[str] = None):
        self.content_url = content_url
        self.width = width
        self.height = height
        self.alternative_text = alternative_text
        self.caption = caption

    @staticmethod
    def from_json(data: dict) -> 'Image':
        return Image(
            content_url=data.get('contentUrl'),
            width=data.get('width'),
            height=data.get('height'),
            alternative_text=data.get('alternativeText'),
            caption=data.get('caption')
           )

    @staticmethod
    def to_json(image: 'Image') -> dict:
        return {
            'contentUrl': image.content_url,
            'width': image.width,
            'height': image.height,
            'alternativeText': image.alternative_text,
            'caption': image.caption
            }


class Category:
    def __init__(self,
                 name: Optional[str] = None,
                 url: Optional[str] = None):
        self.name = name
        self.url = url

    @staticmethod
    def from_json(data: dict) -> 'Category':
        return Category(
            name=data.get('name'),
            url=data.get('url')
          )

    @staticmethod
    def to_json(category: 'Category') -> dict:
        return {
            'name': category.name,
            'url': category.url
        }


class Redirect:
    def __init__(self,
                 name: Optional[str] = None,
                 url: Optional[str] = None):
        self.name = name
        self.url = url

    @staticmethod
    def from_json(data: dict) -> 'Redirect':
        return Redirect(
            name=data.get('name'),
            url=data.get('url')
         )

    @staticmethod
    def to_json(redirect: 'Redirect') -> dict:
        return {
            'name': redirect.name,
            'url': redirect.url
        }


class Template:
    def __init__(self,
                 name: Optional[str] = None,
                 url: Optional[str] = None):
        self.name = name
        self.url = url

    @staticmethod
    def from_json(data: dict) -> 'Template':
        return Template(
            name=data.get('name'),
            url=data.get('url')
        )

    @staticmethod
    def to_json(template: 'Template') -> dict:
        return {
            'name': template.name,
            'url': template.url
        }


class Article:
    def __init__(self,
                 name: Optional[str] = None,
                 abstract: Optional[str] = None,
                 identifier: Optional[int] = None,
                 date_created: Optional[datetime] = None,
                 date_modified: Optional[datetime] = None,
                 date_previously_modified: Optional[datetime] = None,
                 protection: Optional[List[Protection]] = None,
                 version: Optional[Version] = None,
                 previous_version: Optional[PreviousVersion] = None,
                 url: Optional[str] = None,
                 watchers_count: Optional[int] = None,
                 namespace: Optional[Namespace] = None,
                 in_language: Optional[Language] = None,
                 main_entity: Optional[Entity] = None,
                 additional_entities: Optional[List[Entity]] = None,
                 categories: Optional[List[Category]] = None,
                 templates: Optional[List[Template]] = None,
                 redirects: Optional[List[Redirect]] = None,
                 is_part_of: Optional[Project] = None,
                 article_body: Optional[ArticleBody] = None,
                 license: Optional[List[License]] = None,
                 visibility: Optional[Visibility] = None,
                 event: Optional[Event] = None,
                 image: Optional[Image] = None):
        self.name = name
        self.abstract = abstract
        self.identifier = identifier
        self.date_created = date_created
        self.date_modified = date_modified
        self.date_previously_modified = date_previously_modified
        self.protection = protection or []
        self.version = version
        self.previous_version = previous_version
        self.url = url
        self.watchers_count = watchers_count
        self.namespace = namespace
        self.in_language = in_language
        self.main_entity = main_entity
        self.additional_entities = additional_entities or []
        self.categories = categories or []
        self.templates = templates or []
        self.redirects = redirects or []
        self.is_part_of = is_part_of
        self.article_body = article_body
        self.license = license or []
        self.visibility = visibility
        self.event = event
        self.image = image

    @staticmethod
    def from_json(data: dict) -> 'Article':
        return Article(
            name=data.get('name'),
            abstract=data.get('abstract'),
            identifier=data.get('identifier'),
            date_created=Article.parse_date(data.get('date_created')),
            date_modified=Article.parse_date(data.get('date_modified')),
            date_previously_modified=Article.parse_date(data.get('date_previously_modified')),
            protection=[Protection.from_json(p) for p in data.get('protection', [])],
            version=Version.from_json(data.get('version')) if data.get('version') else None,
            previous_version=PreviousVersion.from_json(data.get('previous_version')) if data.get('previous_version') else None,
            url=data.get('url'),
            watchers_count=data.get('watchers_count'),
            namespace=Namespace.from_json(data.get('namespace')) if data.get('namespace') else None,
            in_language=Language.from_json(data.get('in_language')) if data.get('in_language') else None,
            main_entity=Entity.from_json(data.get('main_entity')) if data.get('main_entity') else None,
            additional_entities=[Entity.from_json(e) for e in data.get('additional_entities', [])],
            categories=[Category.from_json(c) for c in data.get('categories', [])],
            templates=[Template.from_json(t) for t in data.get('templates', [])],
            redirects=[Redirect.from_json(r) for r in data.get('redirects', [])],
            is_part_of=Project.from_json(data.get('is_part_of')) if data.get('is_part_of') else None,
            article_body=ArticleBody.from_json(data.get('article_body')) if data.get('article_body') else None,
            license=[License.from_json(l) for l in data.get('license', [])],
            visibility=Visibility.from_json(data.get('visibility')) if data.get('visibility') else None,
            event=Event.from_json(data.get('event')) if data.get('event') else None,
            image=Image.from_json(data.get('image')) if data.get('image') else None,
        )

    @staticmethod
    def to_json(article: 'Article') -> dict:
        return {
            'name': article.name,
            'abstract': article.abstract,
            'identifier': article.identifier,
            'date_created': article.date_created.strftime('%Y-%m-%dT%H:%M:%SZ') if article.date_created else None,
            'date_modified': article.date_modified.strftime('%Y-%m-%dT%H:%M:%SZ') if article.date_modified else None,
            'date_previously_modified': article.date_previously_modified.strftime('%Y-%m-%dT%H:%M:%SZ') if article.date_previously_modified else None,
            'protection': [Protection.to_json(p) for p in article.protection],
            'version': Version.to_json(article.version) if article.version else None,
            'previous_version': PreviousVersion.to_json(article.previous_version) if article.previous_version else None,
            'url': article.url,
            'watchers_count': article.watchers_count,
            'namespace': Namespace.to_json(article.namespace) if article.namespace else None,
            'in_language': Language.to_json(article.in_language) if article.in_language else None,
            'main_entity': Entity.to_json(article.main_entity) if article.main_entity else None,
            'additional_entities': [Entity.to_json(e) for e in article.additional_entities],
            'categories': [Category.to_json(c) for c in article.categories],
            'templates': [Template.to_json(t) for t in article.templates],
            'redirects': [Redirect.to_json(r) for r in article.redirects],
            'is_part_of': Project.to_json(article.is_part_of) if article.is_part_of else None,
            'article_body': ArticleBody.to_json(article.article_body) if article.article_body else None,
            'license': [License.to_json(l) for l in article.license],
            'visibility': Visibility.to_json(article.visibility) if article.visibility else None,
            'event': Event.to_json(article.event) if article.event else None,
            'image': Image.to_json(article.image) if article.image else None,
        }

    @staticmethod
    def parse_date(date_str: Optional[str]) -> Optional[datetime]:
        if date_str:
            return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
        return None
