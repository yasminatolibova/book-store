from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class StandardResultsPagination(PageNumberPagination):
   
    page_size = 10

    page_size_query_param = 'page_size'
    
    
    def get_paginated_response(self, data):
        
        return Response({
            'count': self.page.paginator.count,           
            'total_pages': self.page.paginator.num_pages, 
            'current_page': self.page.number,                             
            'next': self.get_next_link(),                 
            'previous': self.get_previous_link(), 
            'page_size': self.page_size,          
            'results': data                              
        })


