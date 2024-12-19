using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LODtester : MonoBehaviour
{
    public bool enableLOD;

    private LODGroup[] LODGroups; 
    void Start()
    {   
        LODGroups = FindObjectsOfType<LODGroup>();
    }
    void Update()
    {
        if(Input.GetKey(KeyCode.L)){
            enableLOD = !enableLOD;
        }
         
        if(LODGroups[0].enabled == enableLOD){
            return;
        }
        else{
            foreach(LODGroup lod in LODGroups){
                lod.enabled = enableLOD;
            }
        }
    }
}
