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

from workflowData.Data2.func1 import func11
from workflowData.Data2.func2 import func22
from workflowData.Data2.func3 import func33


from workflowData.Data3.func1 import func111
from workflowData.Data3.func3 import func333
from workflowData.Data3.func4 import func444


from Physical_Capability import funcPreIlyas,funcIlyas,funcIlyas1

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
    funcPreIlyas()
    print("Prétraitement terminé !")


@app.get("/gps/func1")
def get_func1_plot():
    """Endpoint pour la visualisation func1"""
    fig = func1()
    
    # Convertir en image PNG
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")

@app.get("/gps/func2")
def get_func2_plot():
    """Endpoint pour la visualisation func2"""
    fig = func2()
    
    # Convertir en base64 pour une intégration facile
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")

@app.get("/gps/func3")
def get_func3_plot():
    """Endpoint pour la visualisation func3"""
    fig = func3()
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")


@app.get("/BioPlayer/func1")
def get_func3_plot():
    """Endpoint pour la visualisation func11"""
    fig = func11()
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")


@app.get("/BioPlayer/func2")
def get_func3_plot():
    """Endpoint pour la visualisation func22"""
    fig = func22()
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")



@app.get("/BioPlayer/func3")
def get_func3_plot():
    """Endpoint pour la visualisation func33"""
    fig = func33()
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")


@app.get("/IndPriority/func1")
def get_func3_plot():
    """Endpoint pour la visualisation func111"""
    fig = func111()
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")



@app.get("/IndPriority/func2")
def get_func3_plot():
    """Endpoint pour la visualisation func222"""
    fig = func333()
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")


@app.get("/IndPriority/func3")
def get_func3_plot():
    """Endpoint pour la visualisation func444"""
    df = func444()
    
    # Convertir le DataFrame en figure matplotlib
    fig, ax = plt.subplots(figsize=(13, 3))
    ax.axis('off')  # Cacher les axes
    
    # Créer un tableau
    table = ax.table(
        cellText=df.values,
        rowLabels=df.index,
        colLabels=df.columns,
        cellLoc='center',
        loc='center'
    )
    
    # Ajuster la taille des cellules
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 1.5)
    
    plt.title('Tracking vs Target')
    plt.tight_layout()
    
    # Sauvegarder en image
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")


@app.get("/PhsCap/func1")
def get_func3_plot():
    """Endpoint pour la visualisation funcIlyas"""
    fig = funcIlyas1()
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")


@app.get("/PhsCap/func2")
def get_func3_plot():
    """Endpoint pour la visualisation funcIlyas"""
    fig = funcIlyas()
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
    plt.close(fig)
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)