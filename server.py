import asyncio
from aiohttp import web

routes = web.RouteTableDef()

@routes.post('/receive_json')
async def handle_post(request):
    try:
        # Ricevi il corpo della richiesta come JSON
        data = await request.json()
        
        # Puoi processare il dato JSON ricevuto qui
        # Ad esempio, stampare il dato ricevuto
        print("Dati ricevuti:", data)
        
        # Risposta in formato JSON
        return web.json_response({'message': 'JSON ricevuto con successo', 'data': data})
    except Exception as e:
        return web.json_response({'error': str(e)}, status=400)

async def init_app() -> web.Application:
    app = web.Application()
    app.add_routes(routes)
    return app

# Esegui l'app
if __name__ == "__main__":
    app = asyncio.run(init_app())
    web.run_app(app)
