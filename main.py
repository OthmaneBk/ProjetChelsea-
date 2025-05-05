from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import matplotlib.pyplot as plt
import io
import uvicorn
from workflowData.Data1.pretretement import pretretement
from workflowData.Data1.func1 import func1
from workflowData.Data1.func2 import func2
from workflowData.Data1.func3 import func3

app = FastAPI(title="GPS Data Visualization API")


# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


async def startup_event():
    """Exécute le prétraitement automatiquement au lancement de l'API"""
    print("Exécution du prétraitement des données...")
    pretretement()  # Assurez-vous que pretretement accepte data_gps en paramètre
    print("Prétraitement terminé !")


@app.get("/visualization/func1")
def get_func1_plot():
    """Endpoint pour la visualisation func1"""
    fig = func1()
    
    # Convertir en image PNG
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")

@app.get("/visualization/func2")
def get_func2_plot():
    """Endpoint pour la visualisation func2"""
    fig = func2()
    
    # Convertir en base64 pour une intégration facile
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")

@app.get("/visualization/func3")
def get_func3_plot():
    """Endpoint pour la visualisation func3"""
    fig = func3()
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)