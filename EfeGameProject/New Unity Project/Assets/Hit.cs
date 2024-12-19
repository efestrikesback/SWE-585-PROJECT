using UnityEngine;
using Mirror;

public class Hit : NetworkBehaviour
{
    public float lifeTime = 5f;

    void Start()
    {
        // Destroy the bullet after its lifetime expires
        Invoke(nameof(DestroySelf), lifeTime);
    }

    void DestroySelf()
    {
        // Only the server can destroy networked objects
        if (isServer)
        {
            NetworkServer.Destroy(gameObject);
        }
    }

    // This function is called when the bullet collides with another collider
    void OnTriggerEnter(Collider other)
    {
        // Ensure that only the server handles collision logic
        if (!isServer && isLocalPlayer)
            return;

        // Check if the bullet hit a player
        if (other.CompareTag("Player"))
        {
            // Destroy the player across the network
            NetworkServer.Destroy(other.gameObject);

            // Destroy the bullet
            NetworkServer.Destroy(gameObject);
        }
    }
}
